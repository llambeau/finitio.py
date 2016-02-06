from ..support.decorators import TypeType
from .collection_type import CollectionType
from ..exceptions import UndressError


@TypeType("set", ['element_type', 'metadata'])
class SetType(CollectionType):

    def _include(self, value, world):
        if not isinstance(value, set) and not isinstance(value, list):
            return False

        if not all(self.element_type.include(v, world) for v in value):
            return False

        return True

    def _m_dress(self, value, monad):
        if not isinstance(value, set) and not isinstance(value, list):
            msg = 'set/list expected, got `{0}`'.format(value)
            return monad.failure(self, [msg, [value]])

        def mapper(elm, _idx):
            return self.element_type.m_dress(elm, monad)

        def on_failure(causes):
            msg = "Invalid ${typeName}"
            return monad.failure(self, [msg, ["Set"]], causes)

        m = monad.map(list(value), mapper, on_failure)

        def finalise(_set):
            duplicates = set([x for x in _set if _set.count(x) > 1])
            if len(duplicates):
                msg = "Duplicate values: `${duplicates}`"
                dupstr = [str(dup) for dup in duplicates]
                err = monad.failure(self, [msg, [', '.join(dupstr)]])

                def cause_failure(cause):
                    return monad.failure(self, "Invalid Set", [cause])

                return err.on_failure(cause_failure)
            else:
                return m

        return m.on_success(finalise)

    def _undress(self, value, as_type):
        if not isinstance(as_type, CollectionType):
            raise UndressError('Unable to undress `{0}` to `{1}'
                               .format(value, as_type))
        return super(self, SetType).undress(value, as_type)

    def low(self):
        return SetType(self.element_type.low())

    def resolve_proxies(self, system):
        return self.element_type.resolve_proxies(system)

    def __repr__(self):
        return '{' + '{0}'.format(self.element_type) + '}'
