import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Test suite for the Calculator class in pkg.calculator.
    """

    def setUp(self):
        """
        Set up a new Calculator instance before each test method.
        """
        self.calculator = Calculator()

    def test_addition(self):
        """
        Test basic addition.
        """
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        """
        Test basic subtraction.
        """
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        """
        Test basic multiplication.
        """
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self):
        """
        Test basic division.
        """
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self):
        """
        Test expressions with multiple operations and operator precedence.
        """
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self):
        """
        Test a more complex expression with mixed operators.
        """
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self):
        """
        Test evaluation with an empty string expression, expecting a ValueError.
        """
        with self.assertRaises(ValueError):
            self.calculator.evaluate("")

    def test_invalid_operator(self):
        """
        Test evaluation with an unsupported operator, expecting a ValueError.
        """
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self):
        """
        Test evaluation with insufficient operands for an operator, expecting a ValueError.
        """
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    def test_division_by_zero(self):
        """
        Test division by zero, expecting a ZeroDivisionError.
        """
        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate("10 / 0")

    def test_parentheses_basic(self):
        """
        Test basic parentheses for grouping.
        """
        result = self.calculator.evaluate("(3 + 5) * 2")
        self.assertEqual(result, 16)

    def test_parentheses_nested(self):
        """
        Test nested parentheses.
        """
        result = self.calculator.evaluate("((10 - 2) / 4) + 1")
        self.assertEqual(result, 3)

    def test_parentheses_with_precedence(self):
        """
        Test parentheses overriding normal precedence.
        """
        result = self.calculator.evaluate("3 + (4 * 5)")
        self.assertEqual(result, 23)

    def test_mismatched_opening_parenthesis(self):
        """
        Test an expression with a missing closing parenthesis.
        """
        with self.assertRaises(ValueError) as cm:
            self.calculator.evaluate("(3 + 5")
        self.assertIn("Mismatched parentheses", str(cm.exception))

    def test_mismatched_closing_parenthesis(self):
        """
        Test an expression with an extra closing parenthesis.
        """
        with self.assertRaises(ValueError) as cm:
            self.calculator.evaluate("3 + 5)")
        self.assertIn("Mismatched parentheses", str(cm.exception))

    def test_no_spaces(self):
        """
        Test expressions with no spaces between tokens.
        """
        result = self.calculator.evaluate("3+5*2")
        self.assertEqual(result, 13) # 3 + (5 * 2)

    def test_mixed_spaces(self):
        """
        Test expressions with mixed spaces between tokens.
        """
        result = self.calculator.evaluate(" ( 3 + 5 ) * 2 ")
        self.assertEqual(result, 16)

if __name__ == "__main__":
    unittest.main()
