import unittest
from tools.calculator_tool import CalculatorTool


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        calc = CalculatorTool()
        self.assertEqual(calc.calculate("2+2"), 4)

    def test_multiplication(self):
        calc = CalculatorTool()
        self.assertEqual(calc.calculate("5*3"), 15)


if __name__ == "__main__":
    unittest.main()