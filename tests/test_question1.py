"""
Unit tests for Question 1 (maximize_revenue and pin_policy)
"""
import unittest
from question1.maximize_revenue import maximize_capital
from question1.pin_policy import min_changes_for_strong_pin

class TestQuestion1(unittest.TestCase):
    def test_maximize_capital(self):
        self.assertEqual(maximize_capital(2, 0, [2, 5, 8], [0, 2, 3]), 7)
        self.assertEqual(maximize_capital(3, 1, [3, 6, 10], [1, 3, 5]), 19)
        self.assertEqual(maximize_capital(1, 0, [1], [0]), 1)

    def test_min_changes_for_strong_pin(self):
        self.assertEqual(min_changes_for_strong_pin("X1!"), 3)
        self.assertEqual(min_changes_for_strong_pin("123456"), 2)
        self.assertEqual(min_changes_for_strong_pin("Aa1234!"), 0)

if __name__ == "__main__":
    unittest.main()
