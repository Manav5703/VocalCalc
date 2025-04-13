import unittest
from calculator import Calculator
from command_parser import CommandParser

class TestCalculatorFunctions(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
        self.parser = CommandParser()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 3), 0.33)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(5, 0), "Error: Division by zero")

    def test_logarithm(self):
        self.assertEqual(self.calc.logarithm(100), 2)
        self.assertEqual(self.calc.logarithm(1), 0)
        self.assertEqual(self.calc.logarithm(0), "Error: Logarithm of non-positive number")
        self.assertEqual(self.calc.logarithm(-5), "Error: Logarithm of non-positive number")

    def test_square_root(self):
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(2), 1.41)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertEqual(self.calc.square_root(-1), "Error: Square root of negative number")

    def test_cube_root(self):
        self.assertEqual(self.calc.cube_root(27), 3)
        self.assertEqual(self.calc.cube_root(-8), -2)
        self.assertEqual(self.calc.cube_root(0), 0)

    def test_exponentiation(self):
        self.assertEqual(self.calc.exponentiation(2, 3), 8)
        self.assertEqual(self.calc.exponentiation(3, 2), 9)
        self.assertEqual(self.calc.exponentiation(5, 0), 1)
        self.assertEqual(self.calc.exponentiation(0, 5), 0)

    def test_trigonometric_functions(self):
        self.assertEqual(self.calc.sine(0), 0)
        self.assertEqual(self.calc.sine(90), 1)
        self.assertEqual(self.calc.cosine(0), 1)
        self.assertEqual(self.calc.cosine(90), 0)
        self.assertEqual(self.calc.tangent(0), 0)
        self.assertEqual(self.calc.tangent(45), 1)

    def test_parse_command_addition(self):
        result, history = self.parser.parse_command("what is 5 plus 3")
        self.assertEqual(result, 8)
        self.assertEqual(history, "5 + 3 = 8")

        result, history = self.parser.parse_command("add 10 and 20")
        self.assertEqual(result, 30)
        self.assertEqual(history, "10 + 20 = 30")

    def test_parse_command_subtraction(self):
        result, history = self.parser.parse_command("what is 10 minus 4")
        self.assertEqual(result, 6)
        self.assertEqual(history, "10 - 4 = 6")

        result, history = self.parser.parse_command("subtract 3 from 8")
        self.assertEqual(result, 5)
        self.assertEqual(history, "8 - 3 = 5")

    def test_parse_command_multiplication(self):
        result, history = self.parser.parse_command("what is 6 times 7")
        self.assertEqual(result, 42)
        self.assertEqual(history, "6 * 7 = 42")

        result, history = self.parser.parse_command("multiply 5 by 5")
        self.assertEqual(result, 25)
        self.assertEqual(history, "5 * 5 = 25")

    def test_parse_command_division(self):
        result, history = self.parser.parse_command("what is 10 divided by 2")
        self.assertEqual(result, 5)
        self.assertEqual(history, "10 / 2 = 5.00")

        result, history = self.parser.parse_command("divide 9 by 3")
        self.assertEqual(result, 3)
        self.assertEqual(history, "9 / 3 = 3.00")

    def test_parse_command_scientific(self):
        result, history = self.parser.parse_command("what is square root of 16")
        self.assertEqual(result, 4)
        self.assertEqual(history, "√(16) = 4")

        result, history = self.parser.parse_command("what is sine of 30")
        self.assertEqual(result, 0.5)
        self.assertEqual(history, "sin(30) = 0.5")

        result, history = self.parser.parse_command("what is log of 100")
        self.assertEqual(result, 2)
        self.assertEqual(history, "log(100) = 2")

if __name__ == '__main__':
    unittest.main()
