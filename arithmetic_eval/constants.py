from operator import add, floordiv, mod, mul, pow, sub, truediv, not_
from ast import (
    Add,
    Div,
    FloorDiv,
    Mod,
    Mult,
    Pow,
    Sub,
    And,
    Or,
    Not,
    operator,
)
from typing import Callable, Dict, Type

ARITHMETIC_OPERATION_TO_OPERATOR: Dict[Type[operator], Callable] = {
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

BOOLEAN_BIN_OPERATION_TO_OPERATOR: Dict[Type[operator], Callable] = {
    And: lambda left, right: bool(left) and bool(right),
    Or: lambda left, right: bool(left) or bool(right),
}

BOOLEAN_UNARY_OPERATION_TO_OPERATOR: Dict[Type[operator], Callable] = {
    Not: not_,
}

BOOLEAN_BIN_OPERATIONS = tuple(BOOLEAN_BIN_OPERATION_TO_OPERATOR.keys())
BOOLEAN_UNARY_OPERATIONS = tuple(BOOLEAN_UNARY_OPERATION_TO_OPERATOR.keys())

ARITHMETIC_ERROR_TO_DEFAULT_VALUE: Dict[Type[ArithmeticError], int] = {
    # Built-in exceptions
    FloatingPointError: 0,
    OverflowError: 0,
    ZeroDivisionError: 0,
}
