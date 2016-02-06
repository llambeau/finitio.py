from types import MethodType


def ObjectType(properties, on_dressed=None):
    def decorate(base):
        '''
        Decorate a base class with a new method
        and a classmethod
        '''
        def info(cls, frm):
            args = [frm[p] for p in properties if p is not None]

            instance = cls(*args)
            if on_dressed:
                on_dressed(instance)
            return instance

        def to_info(self):
            return {k: getattr(self, k) for k in properties if k is not None}

        base.info = classmethod(info)
        base.to_info = MethodType(to_info, None, base)
        return base
    return decorate


def TypeType(generator, properties):
    def decorate(base):
        base._generator = generator
        return ObjectType(properties)(base)
    return decorate
