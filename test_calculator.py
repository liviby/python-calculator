import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 8), 13)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(17, 2), 15)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(14, 2), 7)
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()