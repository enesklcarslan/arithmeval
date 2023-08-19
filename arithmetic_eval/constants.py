from operator import add, floordiv, mod, mul, pow, sub, truediv
from ast import Add, Div, FloorDiv, Mod, Mult, Pow, Sub, operator
from typing import Callable

ARITHMETIC_OPERATION_TO_OPERATOR: dict[type[operator], Callable] = {
    # Binary operator tokens
    Add: add,  # +
    Div: truediv,  # /
    FloorDiv: floordiv,  # //
    Mod: mod,  # %
    Mult: mul,  # *
    # MatMult: matmul,  # @
    Pow: pow,  # **
    Sub: sub,  # -
}

ARITHMETIC_OPERATIONS = tuple(ARITHMETIC_OPERATION_TO_OPERATOR.keys())

ARITHMETIC_ERROR_TO_DEFAULT_VALUE: dict[type[ArithmeticError], int] = {
    # Built-in exceptions
    FloatingPointError: 0,
    OverflowError: 0,
    ZeroDivisionError: 0,
}
