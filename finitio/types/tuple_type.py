from . import Type
from ..support.heading import Heading
from ..support import utils
from ..exceptions import UndressError


class TupleType(Type):

    __slots__ = ['_heading']

    def __init__(self, heading, metadata):
        if not isinstance(heading, Heading):
            raise ValueError("Heading expected, got: {0}"
                             .format(heading))

        super(TupleType, self).__init__(metadata)
        self._heading = heading

    def fetch(self, *args):
        return self._heading.fetch(args)

    def _include(self, value, world):
        if not isinstance(value, dict):
            return False

        if not self.are_attributes_valid(value):
            return False

        def valid(attr):
            if attr in value:
                attr_val = value[attr]
                return attr.type.include(attr_val, world)
            else:
                return True

        return all(valid(attr) for attr in self._heading.attributes)

    def _m_dress(self, value, monad):
        if not isinstance(value, dict):
            msg = "Invalid Tuple: `${value}`"
            return monad.failure(self, [msg, [value]])

        result = {}
        success = monad.success(result)

        def callback(_, attr_name):
            attr = self._heading.get_attr(attr_name)
            attr_value = value[attr_name]

            if attr_value is None and attr and attr.required:
                msg = "Missing attribute `${attr_name}`"
                m = monad.failure(attr_name, [msg, [attr_name]])

                def assign(f):
                    f.location = attr_name
                    return m

                m.on_failure(assign)

            elif not attr and not self._heading.allow_extra:
                msg = "Unrecognised attribute `${attr_name}`"
                m = monad.failure(attr_name, [msg, [attr_name]])

                def assign(f):
                    f.location = attr_name
                    return m

                m.on_failure(assign)

            elif attr and attr_value is not None:
                subm = attr.type.m_dress(attr_value, monad)

                def set_error(error):
                    error.location = attr_name
                    return subm

                def assign(val):
                    result[attr_name] = val

                subm.on_failure(set_error)
                subm.on_success(assign)

            elif attr_value is not None:
                result[attr_name] = attr_value
                return success

            else:
                return success

        def on_failure(causes):
            params = ['Tuple', value]
            msg = "Invalid ${typeName}"
            monad.failure(self, [msg, params], causes)

        attributes = self._attributes_hash(self._heading)
        attributes.update(value)
        attributes = attributes.keys()

        monad.refine(success, attributes, callback, on_failure)

    def _undress(self, value, as_type):
        if not isinstance(as_type, TupleType):
            raise UndressError('Tuple cannot undress to `{0}`'
                               .format(as_type))

        [s, l, r] = utils.tri_split(
            self._attributes_hash(self._heading),
            self._attributes_hash(as_type.heading)
        )

        # Left not empty, do we allow projection undressing?
        _req = next(a.required for a in l)
        if _req:
            raise UndressError('Tuple undress does not allow projecting {0}'
                               .format(_req))

        # Right not empty, do we allow missing attributes?
        if len(r) > 0:
            raise UndressError('Tuple undress does not support missing {0}'
                               .format(r))

        # Do we allow disagreements on required?
        if not all(left.required == right.required for left, right in s):
            raise UndressError(
                'Tuple undress requires optional attributes to agree'
                .format(_req))

        # let undress each attributes in turn
        undressed = {}
        for attr in self._heading:
            attr_name = attr.attr_name
            attr_type = attr.attr_type
            attr_value = value[attr_name]
            if attr_value is not None:
                targ_type = as_type.heading.get_attr(attr_name).type
                undressed[attr_name] = attr_type.undress(attr_value, targ_type)

        return undressed

    def _is_super_type_of(self, other):
        return self is other or\
            (isinstance(other, TupleType) and
             self._heading.is_super_type_of(other._heading))

    def __eq__(self, other):
        return self is other or\
            (isinstance(other, TupleType) and
             self._heading == other._heading)

    def low(self):
        return TupleType(self._heading.low())

    def __repr__(self):
        return '{ ' + self._heading + ' }'

    # Private

    def _attributes_hash(self, heading):
        return {attr: attr for attr in heading}

    def attribute_names(self):
        return [attr.name for attr in self._heading.attributes]

    def required_attribute_names(self):
        return [attr.name for attr in self._heading.attributes
                if attr.required]

    def extra_attributes(self, value):
        return set(value.keys()) - self.attribute_names()

    def missing_attributes(self, value):
        return set(self.required_attribute_names()) - set(value.keys())

    def are_attributes_valid(self, value):
        return (self._heading.allow_extra or
                len(self.extra_attributes(value)) == 0) and \
                len(self.missing_attributes(value)) == 0

    def resolve_proxies(self, system):
        return self._heading.resolve_proxies(system)
