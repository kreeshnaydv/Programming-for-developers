"""
Unit tests for Question 2 (weather_anomaly and alphametic_solver)
"""
import unittest
from question2.weather_anomaly import count_anomaly_periods
from question2.alphametic_solver import solve_alphametic

class TestQuestion2(unittest.TestCase):
    def test_weather_anomaly(self):
        self.assertIn(count_anomaly_periods([3, -1, -4, 6, 2], 2, 5), [3, 4])
        self.assertIn(count_anomaly_periods([-2, 3, 1, -5, 4], -1, 2), [4, 5])

    def test_alphametic_solver(self):
        self.assertTrue(solve_alphametic(["STAR", "MOON"], "NIGHT"))
        self.assertFalse(solve_alphametic(["CODE", "BUG"], "DEBUG"))

if __name__ == "__main__":
    unittest.main()
