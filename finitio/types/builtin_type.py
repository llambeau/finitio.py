from . import Type


class BuiltinType(Type):

    __slots__ = ['_py_type']

    def __init__(self, py_type, metadata):
        super(BuiltinType, self).__init__(metadata)
        self._py_type = py_type

    def _m_dress(self, value, monad):
        if self.include(value):
            return monad.success(value)
        else:
            params = [self._py_type.name, value]
            error = 'Invalid ${typeName}: `${value}`'
            return monad.failure(self, [error, params])

    def _include(self, value, monad):
        return isinstance(value, self._py_type)

    def __eq__(self, other):
        return self is other or\
            (isinstance(other, BuiltinType) and
                other._py_type == self._py_type)

    def low(self):
        return self

    def __rep__(self):
        return '.' + self._py_type.name

    def resolve_proxies(self, system):
        pass
