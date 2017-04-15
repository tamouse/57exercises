import unittest
from ex05_simple_maths.simple import *

class TestSimpleMaths(unittest.TestCase):
    def setUp(self):
        self.simple = SimpleMaths(2, 4)

    def test_addition(self):
        self.assertEqual(6, self.simple.add())

    def test_subtraction(self):
        self.assertEqual(-2, self.simple.subtract())

    def test_multiplication(self):
        self.assertEqual(8, self.simple.multiply())

    def test_division(self):
        self.assertEqual(2/4, self.simple.divide())


if __name__ == '__main__':
    unittest.main()
