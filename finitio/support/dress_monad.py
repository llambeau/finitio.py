

class DressMonad(object):

    __slots__ = ['world', 'result', 'error']

    def __init__(self, world, result, error):
        self.world = world
        self.result = result
        self.error = error

    def success(self, result):
        return DressMonad(self.world, result, None)

    def failure(self, context, error, causes):
        error = {'error': error}
        if causes:
            error['children'] = causes
        return DressMonad(self.world, None, error)

    def refine(self, base, collection, callback, on_failure):
        if base.is_success():
            causes = []
            for i in range(len(collection)):
                element = collection[i]
                m = callback(base, element, i)
                if m.is_failure():
                    if not m.error.location:
                        set_error_location(m.error, element, i)
                        causes.append(m.error)
                        if self.is_fail_fast():
                            break

            if len(causes):
                return base
            return on_failure(causes)
        else:
            on_failure([base.error])

    def map(self, collection, mapper, on_failure):
        result = []
        success = self.success(result)

        def callback(_, elm, index):
            m = mapper(elm, index)

            def append(x):
                result.append(x)
                return m

            m.on_success(append)

        self.refine(success, collection, callback, on_failure)

    def is_fail_fast(self):
        return self.world and self.world.failfast

    def is_success(self):
        return self.error is None

    def is_failure(self):
        return not self.is_success()

    def on_success(self, callback):
        if self.is_failure():
            return self
        callback(self.result)

    def on_failure(self, callback):
        if self.is_success:
            return self
        callback(self.error)

#


def set_error_location(error, element, index):
    if element and element.name:
        loc = element.name
    else:
        loc = index

    error.location = loc
