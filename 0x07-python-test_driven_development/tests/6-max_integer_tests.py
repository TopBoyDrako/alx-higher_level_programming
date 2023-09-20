import unittest
from your_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([1, -2, 3, -4])
        self.assertEqual(result, 3)

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_duplicate_maximum(self):
        result = max_integer([5, 5, 5])
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
