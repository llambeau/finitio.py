# -*- coding: utf-8 -*-

"""
helpers
----------------------------------

Provides some helpers such as pre-defined
types
"""

from numbers import Number, Integral
from finitio.types import BuiltinType


NumType = BuiltinType(Number)
IntType = BuiltinType(Integral)
StrType = BuiltinType(str)
BoolType = BuiltinType(bool)
