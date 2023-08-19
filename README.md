# arithmeval - Arithmetic Expression Evaluator

[![PyPI Version](https://img.shields.io/pypi/v/arithmeval)](https://pypi.org/project/arithmeval/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

`arithmeval` is a Python package that provides a utility function to evaluate arithmetic expressions, given a dictionary of values. It supports basic arithmetic operations and can handle simple mathematical calculations.
It also supports string concatenation, though it is not intended to be used as a general-purpose expression evaluator, therefore tests for string concatenation are not included.

**Arithmeval is a secure, safety-first expression evaluator. It only supports the following list of operations:**

- Addition (`+`)
- True division (`/`)
- Floor division (`//`)
- Modulus (`%`)
- Multiplication (`*`)
- Exponentiation (`**`)
- Subtraction (`-`)

## Installation

You can install `arithmeval` using `pip`:

```bash
pip install arithmeval
```

## Usage
Import the `evaluate` function from the arithmetic_eval module:

```python
from arithmetic_eval import evaluate
```
Use the evaluate function to calculate the value of an arithmetic expression:

```python
expression = "a + b"
values_dict = {"a": 1, "b": 2}
result = evaluate(expression, values_dict)
print(result)  # Output: 3
```

The evaluate function takes the following arguments:


- `expression (str)`: The arithmetic expression to be evaluated.
- `value_dict (Optional[dict])`: A dictionary containing variable values used in the expression.
- `arithmetic_exception_to_default_value (Optional[dict])`: A dictionary mapping specific arithmetic exceptions to default values.

The function returns an int, float, or str representing the result of the expression.

## Error Handling
The `evaluate` function raises various exceptions in case of errors:

- `SyntaxError`: If the expression is not a valid Python expression.
- `NameError`: If a variable is not defined in the values_dict.
- `NotImplementedError`: If the expression contains an unsupported operation.
- `MaliciousInputError`: If the expression is a malicious input.

## Examples

```python
from arithmetic_eval import evaluate

expression = "2 * (x + y)"
value_dict = {"x": 3, "y": 4}
result = evaluate(expression, value_dict)
print(result)  # Output: 14
```

```python
from arithmetic_eval import evaluate

expression = "10 / (a - 5)"
value_dict = {"a": 5}
result = evaluate(
   expression=expression, 
   value_dict=value_dict, 
   arithmetic_exception_to_default_value={
      ZeroDivisionError: 0
   }
)
print(result)  # Output: 0
```

Note that it is not recommended to use the `arithmetic_exception_to_default_value` argument. It is only provided for convenience and should be used with caution. The default behavior for any ArithmeticError is to return 0.
If you insist on overriding the default return value for arithmetic exceptions, make sure to use a dictionary mapping each ArithmeticError to a default value.

A list of arithmetic exceptions can be found [here](https://docs.python.org/3/library/exceptions.html#ArithmeticError).

## License
This package is distributed under the MIT License.

## Contributing
Contributions to arithmeval are welcome! Feel free to open issues or pull requests on the GitHub repository.

## Acknowledgements
This package was inspired by the need for a simple and safe arithmetic expression evaluator in Python.