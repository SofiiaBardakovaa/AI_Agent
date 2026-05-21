class CalculatorTool:
    """
    Tool for performing mathematical calculations.
    """

    def calculate(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception:
            raise ValueError("Invalid mathematical expression.")