import re

REPLACE_REGEX = re.compile('\$\{[a-zA-Z]+\}')


class FinitioException(Exception):
    pass


class FinitioTypeError(FinitioException):

    __slots__ = ['location', 'children']

    def __init__(self, info):
        if 'children' in info:
            self.children = info['children']
        else:
            self.children = None

        if 'location' in info:
            self.location = info['location']
        else:
            self.location = None

        self._root_causes_cache = None
        self._causes_cache = None

        message = compute_message(info)
        super(FinitioTypeError, self).__init__(message)

    def get_located_message(self):
        if self.location:
            return "[{0}] {1}".format(self.location, self.message)
        else:
            return self.message

    def causes(self):
        if self._causes_cache:
            return self._causes_cache
        elif self.children:
            return compute_causes(self)

    def cause(self):
        if self.causes():
            return self.causes()[0]

    def root_causes(self):
        if self._root_causes_cache:
            return self._root_causes_cache
        else:
            return compute_root_causes(self)

    def root_cause(self):
        if self.root_causes():
            rc = self.root_causes()
            return rc[len(rc)-1]


class DressError(FinitioTypeError):
    pass


class UndressError(FinitioException):
    pass


class KeyNotFoundError(FinitioException):
    pass


class Namespace:
    pass


def compute_message(info):
    msg = info['error']
    if isinstance(msg, list):
        [msg, data] = msg
        # TODO: can't we find better than this?
        ns = Namespace()
        ns.i = -1

        def replace(match):
            token = match.group(0)
            ns.i = ns.i + 1
            if token in info:
                return info[token]
            else:
                return data[ns.i]
        return REPLACE_REGEX.sub(replace, msg)
    elif isinstance(msg, str):
        return msg
    else:
        return str(info)


def compute_causes(error):
    def mapper(err):
        err['location'] = append_path(error, err)
        if isinstance(err, FinitioTypeError):
            return err
        elif isinstance(err, FinitioException):
            return FinitioTypeError({
                'error': err.message,
                'location': err.location
            })
        else:
            return FinitioTypeError(err)
    return [mapper(err) for err in error.children]


def append_path(parent, child):
    if 'location' not in child:
        return parent.location
    if not parent.location:
        return child['location']
    return parent.location + '/' + child['location']


def compute_root_causes(error, cache=[]):
    if error.causes():
        for err in error.causes():
            compute_root_causes(err, cache)
    else:
        cache.append(error)
    return cache


__all__ = [
    'FinitioException', 'DressError',
    'UndressError', 'KeyNotFoundError'
]
