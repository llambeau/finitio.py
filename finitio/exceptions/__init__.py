import re

REPLACE_REGEX = re.compile('\$\{[a-zA-Z]+\}')


class FinitioException(Exception):
    pass


class DressError(FinitioException):

    def __init__(self, info):
        message = compute_message(info)
        super(DressError, self).__init__(message)


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

        def replace(token):
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


__all__ = [
    'FinitioException', 'DressError',
    'UndressError', 'KeyNotFoundError'
]
