import unittest
from arithmetic_eval.utils import evaluate
from arithmetic_eval.exceptions import MaliciousInputError


class TestEvaluateFunction(unittest.TestCase):
    def test_valid_addition(self):
        expression = "a + b"
        value_dict = {"a": 1, "b": 2}
        result = evaluate(expression, value_dict)
        self.assertEqual(result, 3)

    def test_invalid_expression(self):
        expression = "a +"
        value_dict = {"a": 1, "b": 2}
        with self.assertRaises(SyntaxError):
            evaluate(expression, value_dict)

    def test_missing_variable(self):
        expression = "a + b"
        value_dict = {"a": 1}
        with self.assertRaises(NameError):
            evaluate(expression, value_dict)

    def test_arithmetic_exception_handling(self):
        expression = "1 / 0"
        value_dict = {}
        result = evaluate(expression, value_dict)
        self.assertEqual(result, 0)  # Default value for ArithmeticError

    def test_unsupported_operation(self):
        expression = "a @ b"
        value_dict = {"a": 5, "b": 2}
        with self.assertRaises(NotImplementedError):
            evaluate(expression, value_dict)

    def test_constant_expression(self):
        expression = "42"
        value_dict = {}
        result = evaluate(expression, value_dict)
        self.assertEqual(result, 42)

    def test_malicious_input(self):
        malicious_expression = "a + __import__('os').system('echo Hello, World!')"
        value_dict = {"a": 1}
        with self.assertRaises(MaliciousInputError):
            evaluate(malicious_expression, value_dict)


if __name__ == "__main__":
    unittest.main()
