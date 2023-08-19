import ast
import typing
from arithmetic_eval.constants import (
    ARITHMETIC_OPERATIONS,
    ARITHMETIC_OPERATION_TO_OPERATOR,
    ARITHMETIC_ERROR_TO_DEFAULT_VALUE,
)
from arithmetic_eval.exceptions import MaliciousInputError


def evaluate(
    expression: typing.Union[str, ast.AST],
    value_dict: typing.Optional[dict] = None,
    arithmetic_exception_to_default_value: dict[
        type[ArithmeticError], int
    ] = ARITHMETIC_ERROR_TO_DEFAULT_VALUE,
) -> int | float | str:
    """Calculates the value of a string expression, given a dictionary of values.

    It only supports arithmetic operations.
    Example for expression: "a + b"
    Example for values_dict: {"a": 1, "b": 2}
    The output will be 3.

    Args:
        expression (str): The string expression to be evaluated.

    Returns:
        int | float | str: The result of the expression.

    Raises:
        SyntaxError: If the expression is not a valid Python expression.
        NameError: If a variable is not defined in the values_dict.
        NotImplementedError: If the expression contains an unsupported operation.
        MaliciousInputError: If the expression is a malicious input.
    """
    value_dict = value_dict or {}

    if isinstance(expression, str):
        try:
            expression = ast.parse(expression)
        except SyntaxError as e:
            raise SyntaxError(f"Invalid expression: {expression}") from e
        expression = ast.Expression(expression.body[0].value)

    if isinstance(expression, ast.Expression):
        expression = expression.body

    if isinstance(expression, ast.BinOp):
        left = evaluate(expression.left, value_dict)
        right = evaluate(expression.right, value_dict)
        op = expression.op
        if isinstance(op, ARITHMETIC_OPERATIONS):
            try:
                # left = float(left)
                # right = float(right)
                return ARITHMETIC_OPERATION_TO_OPERATOR[op.__class__](left, right)
            except ArithmeticError as e:
                try:
                    return arithmetic_exception_to_default_value[type(e)]
                except KeyError:
                    raise e
        else:
            raise NotImplementedError(
                f"Operation {op} not implemented. "
                f"Must be one of {', '.join(map(str, ARITHMETIC_OPERATIONS))}"
            )
    elif isinstance(expression, ast.Name):
        try:
            return value_dict[expression.id]
        except KeyError:
            raise NameError(f"Name '{expression.id}' is not defined.")
    elif isinstance(expression, ast.Constant):
        return expression.value
    else:
        raise MaliciousInputError(f"Expression {expression} is not supported")
