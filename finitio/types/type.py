from ..exceptions import DressError, UndressError
from ..support.monad import Monad


class Type(object):

    __slots__ = ['metadata']

    def __init__(self, metadata):
        self.metadata = metadata

    @staticmethod
    def factor(_from):
        return _from[list(_from.keys())[0]]

    def to_factor(self):
        to = {}
        to[self._generator] = self
        return to

    def include(self, value, world={}):
        return self._include(value, world)

    def _include(self, value, world):
        raise NotImplementedError('`_include` not implemented')

    def dress(self, value, world={}):
        monad = self.m_dress(value, Monad(world))
        if monad.is_success():
            return monad.result
        else:
            raise DressError(monad.error)

    def m_dress(self, value, monad):
        return self._m_dress(value, monad)

    def _m_dress(self, value, monad):
        raise NotImplementedError('`_m_dress` not implemented')

    def undress(self, value, as_type):
        return self._undress(value, as_type.true_one())

    def _undress(self, value, as_type):
        if as_type.is_super_type_of(self):
            return value

        if as_type.include(value):
            return value

        raise UndressError("Unable to undress `{0}` from {1} to `{2}`"
                           .format(value, self, as_type))

    def is_super_type_of(self, other):
        return self._is_super_type_of(other)

    def _is_super_type_of(self, other):
        raise NotImplementedError('`_is_super_type_of` not implemented')

    def _is_sub_type_of(self, other):
        return False

    def fetch_type(self):
        return self

    def is_fake(self):
        return False

    def true_one(self):
        return self

    def __eq__(self, other):
        return isinstance(other, Type)

    def __ne__(self, other):
        return not self.__eq__(other)
