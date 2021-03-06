from . import Type
from ..support.decorators import TypeType


@TypeType("builtin", ['metadata'])
class AnyType(Type):

    def __init__(self, metadata=None):
        super(AnyType, self).__init__(metadata)

    def _m_dress(self, value, monad):
        return monad.success(value)

    def _include(self, value, world):
        return True

    def _is_super_type_of(self, other):
        return True

    def __eq__(self, other):
        return isinstance(other, AnyType) or super(AnyType, self).__eq__(other)

    def low(self):
        return self

    def resolve_proxies(self):
        pass

    def __repr__(self):
        return '.'
