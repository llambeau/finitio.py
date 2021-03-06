from ..types.type import Type


class CollectionType(Type):

    __slots__ = ['name', 'element_type']

    def __init__(self, element_type, metadata=None, name=None):
        if not isinstance(element_type, Type):
            raise ValueError('Finitio.Type expected, got: {0}'
                             .format(element_type))
        self.name = name
        self.element_type = element_type
        super(CollectionType, self).__init__(metadata)

    def __eq__(self, other):
        return self is other\
            or (isinstance(other, type(self)) and
                self.element_type == other.element_type)

    def _is_super_type_of(self, other):
        return self is other\
            or (isinstance(other, type(self)) and
                self.element_type.is_super_type_of(other.element_type))

    def _undress(self, value, as_type):
        _from = self.element_type
        _to = as_type.element_type

        if _to.is_super_type_of(_from):
            return value

        return [_from.undress(v, _to) for v in value]
