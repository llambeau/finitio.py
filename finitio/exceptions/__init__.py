class FinitioException(Exception):
    pass


class DressError(FinitioException):
    pass


class UndressError(FinitioException):
    pass


class KeyNotFoundError(FinitioException):
    pass


__all__ = [
    'FinitioException', 'DressError',
    'UndressError', 'KeyNotFoundError'
]
