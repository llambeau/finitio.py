from __future__ import unicode_literals

from arpeggio import ZeroOrMore, ParserPython, Optional
from arpeggio import RegExMatch as _

# Grammar

# LITERALS


def literal():
    return [
        string_literal,
        range_literal,
        real_literal,
        integer_literal,
        boolean_literal,
        array_literal,
        set_literal,
        regexp_literal,
        function_literal
    ]


def string_literal():
    return _('["]([\\"]|!["].)*["]')


def range_literal():
    return [
        (integer_literal, '..', integer_literal),
        (integer_literal, '...', integer_literal),
        (integer_literal, '..')
    ]


def function_literal():
    return '&', js_identifier


def js_identifier():
    return _("[a-zA-Z$_][a-zA-Z0-9$_]*"),\
        ZeroOrMore(".", _("[a-zA-Z$_][a-zA-Z0-9$_]*"))


def integer_literal():
    return [_('[1-9][0-9]*'), _('[0]'), _('-[1-9][0-9]*')]


def real_literal():
    return Optional(integer_literal), '.', _('[0-9]+')


def array_literal():
    return '[', literal, ZeroOrMore(opt_comma, literal), ']'


def set_literal():
    return [
        ('{', literal, ZeroOrMore(opt_comma, literal), '}'),
        ('{', '}')
    ]


def boolean_literal():
    return ["true", "false"]


def regexp_literal():
    return "not implemented yet"

# LEXER (names)


def var_name():
    return _('[a-z]+')


def contract_name():
    return _('[a-z][a-zA-Z_]*')


def constraint_name():
    return _('[a-z][a-zA-Z0-9_]*')


def attribute_name():
    return _('[a-z$_][a-zA-Z0-9_]*')


def type_name():
    return Optional(type_qualifier, '.'), _('[A-Z]'), _('[a-zA-Z:*')


def type_qualifier():
    return _('[a-z][a-z0-9]*')


def builtin_type_name():
    return _('[a-zA-Z0-9:.]+')


# LEXER (spacing, symbols and comments)


def dots():
    return '...'


def pipe():
    return '|'


def comma():
    return ','


def opt_comma():
    return Optional(comma)


def comment():
    return [_("//.*"), _("/\*.*\*/")]


parser = ParserPython(literal)
# system = "[1, 2]"
# result = parser.parse(system)
# print result
