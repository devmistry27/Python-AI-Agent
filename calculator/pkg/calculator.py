import re

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def _tokenize(self, expression: str) -> list[str]:
        """
        Tokenizes the input expression, recognizing numbers, operators, and parentheses.
        """
        # Regular expression to match numbers (integers or floats), operators, and parentheses.
        # It handles cases like "3 + 5", "3+5", " ( 3 + 5 ) "
        token_pattern = re.compile(r'(\d+\.?\d*|\+|\-|\*|\/|\(|\))')
        tokens = token_pattern.findall(expression)
        if not tokens:
            raise ValueError("No valid tokens found in the expression.")
        return [token.strip() for token in tokens if token.strip()]

    def evaluate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression given as a string.
        Raises ValueError for invalid expressions or tokens.
        """
        if not expression or expression.isspace():
            raise ValueError("Expression cannot be empty or contain only whitespace.")

        tokens = self._tokenize(expression)
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens: list[str]) -> float:
        """
        Evaluates an infix expression represented as a list of tokens
        using the Shunting-yard algorithm principles, now supporting parentheses.
        """
        operand_stack = []
        operator_stack = []

        for token in tokens:
            if token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self._apply_operator(operator_stack, operand_stack)
                if not operator_stack:
                    raise ValueError("Mismatched parentheses: No opening parenthesis found.")
                operator_stack.pop()  # Pop the opening parenthesis
            elif token in self.operators:
                while (
                    operator_stack
                    and operator_stack[-1] in self.operators
                    and self.precedence[operator_stack[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operator_stack, operand_stack)
                operator_stack.append(token)
            else:
                try:
                    operand_stack.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid token: {token}")

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses: Unclosed opening parenthesis.")
            self._apply_operator(operator_stack, operand_stack)

        if len(operand_stack) != 1:
            raise ValueError("Invalid expression format or unmatched operators/operands.")

        return operand_stack[0]

    def _apply_operator(self, operator_stack: list[str], operand_stack: list[float]):
        """
        Pops an operator from the operator stack and two operands from the operand stack,
        performs the operation, and pushes the result back onto the operand stack.
        """
        if not operator_stack:
            return

        operator = operator_stack.pop()
        if len(operand_stack) < 2:
            raise ValueError(f"Not enough operands for operator {operator}")

        operand_b = operand_stack.pop()
        operand_a = operand_stack.pop()

        if operator == '/' and operand_b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        operand_stack.append(self.operators[operator](operand_a, operand_b))
