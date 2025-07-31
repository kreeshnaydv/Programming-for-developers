"""
Unit tests for Question 3 (pattern_sequence and magical_words)
"""
import unittest
from question3.pattern_sequence import max_pattern_extraction
from question3.magical_words import max_magical_power

class TestQuestion3(unittest.TestCase):
    def test_pattern_sequence(self):
        self.assertEqual(max_pattern_extraction("bca", 6, "ba", 3), 3)

    def test_magical_words(self):
        self.assertEqual(max_magical_power("xyzyxabc"), 5)
        self.assertEqual(max_magical_power("levelwowracecar"), 35)

if __name__ == "__main__":
    unittest.main()
