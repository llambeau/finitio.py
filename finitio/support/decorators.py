

def ObjectType(properties, on_dressed=None):
    def decorate(base):
        def info(cls, frm):
            args = [frm[p] for p in properties if p is not None]

            instance = cls(*args)
            if on_dressed:
                on_dressed(instance)
            return instance

        base.info = classmethod(info)
        return base
    return decorate


def TypeType(generator, properties):
    def decorate(base):
        base._generator = generator
        return ObjectType(properties)(base)
    return decorate
