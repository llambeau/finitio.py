from . import Type


class TypeDef(Type):

    __slots__ = ['_type', '_name']

    def __init__(self, typ, name, metadata):
        if not name:
            raise ValueError('`name` cannot be None on TypeDef')

        super(TypeDef, self).__init__(metadata)

        self._name = name
        self._type = typ

    def fetch(self, *args):
        return self._type.fetch(args)

    def _include(self, value, world):
        return self._type.include(value, world)

    def _m_dress(self, value, monad):
        m = self._type.m_dress(value, monad)

        def func(cause):
            if self._name == "Main":
                cause.type_name = 'Data'
            else:
                cause.type_name = self._name
            return m

        return m.on_failure(func)

    def _undress(self, value, as_type):
        return self._type.undress(value, as_type)

    def _is_super_type_of(self, child):
        return self._type.is_super_type_of(child)

    def _is_sub_type_of(self, sup):
        return self._type.is_sub_type_of(sup)

    def __eq__(self, other):
        return self._type == other

    def is_fake(self):
        return True

    def true_one(self):
        return self._type

    def low(self):
        return self._type.low()

    def resolve_proxies(self, system):
        return self._type.resolve_proxies(system)

    def __rep__(self):
        return self._name
