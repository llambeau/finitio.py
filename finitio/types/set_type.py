from sets import Set
from ..support import CollectionType
from ..exceptions import UndressError


class SetType(CollectionType):

    def _include(self, value, world):
        if not isinstance(value, Set):
            return False

        if not all(self._element_type.include(v, world) for v in value):
            return False

        return True

    def _m_dress(self, value, monad):
        if not isinstance(value, Set):
            msg = 'Set expected, got `{0}`'.format(value)
            return monad.failure(self, [msg, [value]])

        def mapper(elm):
            self._element_type.mDress(elm, monad)

        def on_failure(causes):
            msg = "Invalid ${typeName}"
            monad.failure(self, [msg, ["Set"]], causes)

        return monad.map(value, mapper, on_failure)

    def _undress(self, value, as_type):
        if not isinstance(as_type, CollectionType):
            raise UndressError('Unable to undress `{0}` to `{1}'
                               .format(value, as_type))
        return super(self, SetType).undress(value, as_type)

    def low(self):
        return SetType(self._element_type.low())

    def resolve_proxies(self, system):
        return self._element_type.resolve_proxies(system)

    def __repr__(self):
        return '{' + self._element_type + '}'
