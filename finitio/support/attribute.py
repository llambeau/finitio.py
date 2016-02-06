from ..exceptions import KeyNotFoundError
from ..type import Type


class Attribute(object):

    __slots__ = ['name', 'type', 'required', 'metadata']

    def __init__(self, name, typ, required=True, metadata=None):
        if not isinstance(name, str):
            raise ValueError('String expected for attribute name, '
                             'got: {0}'.format(name))

        if not isinstance(required, bool):
            raise ValueError('Boolean expected for attribute required, '
                             'got: {0}'.format(required))

        if not isinstance(typ, Type):
            raise ValueError('Type expected for attribute typ, '
                             'got: {0}'.format(typ))

        self.name = name
        self.type = typ
        self.metadata = metadata
        self.required = required

    def fetch_type(self):
        return self.type

    def fetch_on(self, arg, callback=None):
        if not isinstance(arg, dict):
            raise ValueError('Dict expected, got {0}'.format(arg))

        if self.name not in arg:
            if callback:
                return callback()
            else:
                raise KeyNotFoundError('Key `{0}` not found'
                                       .format(self.name))

        return arg[self.name]

    def is_super_attribute_of(self, other):
        return self is other or\
            (self.name == other.name and
                (not self.required or other.required) and
                self.type.is_super_type_of(other.type))

    def __eq__(self, other):
        return self is other or\
            (isinstance(other, Attribute) and
                self.name == other.name and
                self.required == other.required and
                self.type == other.type)

    def low(self):
        return Attribute(self.name, self.type.low(), self.required)

    def resolve_proxies(self, system):
        return self.type.resolve_proxies(system)

    def __repr__(self):
        if self.required:
            return '{0} : {1}'.format(self.name, self.type)
        else:
            return '{0} :? {1}'.format(self.name, self.type)
