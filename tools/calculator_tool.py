class CalculatorTool:

    def calculate(self, expression):
        """
            Tool used for mathematical calculations.
        """
        try:
            return eval(expression)

        except Exception:
            raise ValueError("Invalid expression")