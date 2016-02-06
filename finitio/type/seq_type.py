from ..support import CollectionType
from ..exceptions import UndressError


class SeqType(CollectionType):

    def _include(self, value, world):
        if not isinstance(value, list):
            return False

        if not all(self._element_type.include(v, world) for v in value):
            return False

        return True

    def _m_dress(self, value, monad):
        if not isinstance(value, list):
            msg = 'List expected, got `${value}`'
            return monad.failure(self, [msg, [value]])

        def mapper(elm):
            self._element_type.mDress(elm, monad)

        def on_failure(causes):
            msg = "Invalid ${typeName}"
            monad.failure(self, [msg, ["Sequence"]], causes)

        return monad.map(value, mapper, on_failure)

    def _undress(self, value, as_type):
        if not isinstance(as_type, SeqType):
            raise UndressError('Unable to undress `{0}` to `{1}'
                               .format(value, as_type))
        return super(self, SeqType).undress(value, as_type)

    def low(self):
        return SeqType(self._element_type.low())

    def resolve_proxies(self, system):
        return self._element_type.resolve_proxies(system)

    def __repr__(self):
        return '[' + self._element_type + ']'
