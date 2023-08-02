import unittest
from app import add, subtract, multiply, divide

class TestApp(unittest.TestCase):

    def test_add(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiply(self):
        result = multiply(2, 4)
        self.assertEqual(result, 8)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
