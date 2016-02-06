from . import Type
from ..exceptions import UndressError


class UnionType(Type):

    __slots__ = ['_candidates']

    def __init__(self, candidates, metadata):
        for item in candidates:
            if not isinstance(item, Type):
                raise ValueError('Finitio.Type expected, got: {0}'
                                 .format(item))

        super(UnionType, self).__init__(metadata)
        self._candidates = candidates

    def _m_dress(self, value, monad):

        def callback(candidate):
            return candidate.m_dress(value, monad)

        def on_failure(causes):
            params = ['value', value]
            msg = 'Invalid ${typeName}: `${value}`'
            monad.failure(self, [msg, params], causes)

        return monad.find(self._candidates, callback, on_failure)

    def _undress(self, value, as_type):
        if self is as_type:
            return value

        # find a candidate which is a subtype of as_type
        using = next(c for c in self._candidates
                     if as_type.is_super_type_of(c))
        if using:
            return using.undress(value, as_type)

        # find a candidate that includes value
        using = next(c for c in self._candidates
                     if c.include(value))
        if using:
            return using.undress(value, as_type)

        raise UndressError('Unable to dress `{0}` to `{1}'
                           .format(value, as_type))

    def _include(self, value, world):
        return any(c for c in self._candidates
                   if c.include(value)) is not None

    def _is_super_type_of(self, other):
        return self is other or\
            any(c for c in self._candidates
                if c.is_super_type_of(other)) or\
            (isinstance(other, UnionType) and
                all(any(c for c in self._candidates if c.is_super_type_of(d))
                    for d in other._candidates))

    def __eq__(self, other):
        return self is other or\
            (isinstance(other, UnionType) and
                self._candidates_eq(other, True)) or\
            super(UnionType, self).__eq__(other)

    def _candidates_eq(self, other, and_back=False):
        if not all(any(c2 for c2 in other._candidates if c.equals(c2))
                   for c in self._candidates):
            return False

        if and_back:
            return UnionType._candidates_eq(other, self, False)

    def low(self):
        raise NotImplementedError('UnionType#low is not defined yet, sorry!')

    def resolve_proxies(self, system):
        return [c.resolve_proxies(system) for c in self._candidates]

    def __repr__(self):
        return ', '.join([str(c) for c in self._candidates])
