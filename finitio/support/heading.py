import copy
from . import Attribute
from . import utils


class Heading(object):

    DEFAULT_OPTS = {
        'allow_extra': False
    }

    __slots__ = ['allow_extra', 'attributes', 'options']

    def __init__(self, attributes, options=DEFAULT_OPTS):
        if not isinstance(attributes, set):
            raise ValueError('Set of Attribute expected')

        if not all(isinstance(attr, Attribute) for attr in attributes):
            raise ValueError('Set of Attribute expected')

        if not isinstance(options, dict):
            raise ValueError('Dict of options expected')

        self.allow_extra = options['allow_extra']
        self.attributes = attributes
        self.options = options

    def get_attr(self, name):
        return next(attr for attr in self.attributes if attr.name == name)

    def size(self):
        return len(self.attributes)

    def is_emtpy(self):
        return self.size() == 0

    def multi(self):
        return self.allow_extra or \
               any(not a.required for a in self.attributes)

    def __iter__(self):
        return self.attributes.__iter__()

    def __repr__(self):
        _repr = ', '.join([str(attr) for attr in self.attributes])
        if self.allow_extra:
            _repr += '...'
        return _repr

    def names(self):
        return [attr.name for attr in self.attributes]

    def is_super_heading_of(self, other):
        if self is other:
            return True

        if not isinstance(other, Heading):
            return False

        [s, l, r] = utils.tri_split(
            attributes_by_name(self),
            attributes_by_name(other),
        )

        return (
            all(left.isSuperAttributeOf(right) for left, right in s) and
            all(not attr.required for attr in l) and
            (self.allow_extra or not other.allow_extra) and
            (self.allow_extra or len(r) == 0)
        )

    def __eq__(self, other):
        return self is other or\
            (isinstance(other, Heading) and
                self.attributes == other.attributes and
                self.options == other.options)

    def low(self):
        reattrs = [attr.low for attr in self.attributes]
        return Heading(reattrs, copy.deepcopy(self.options))

    def resolve_proxies(self, system):
        return [attr.resolve_proxies(system) for attr in self.attributes]

#


def attributes_by_name(attributes):
    return {attr.name: attr for attr in attributes}
