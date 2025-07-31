"""
Unit tests for Question 4 (secure_transmission and treasure_hunt)
"""
import unittest
from question4.secure_transmission import SecureTransmission
from question4.treasure_hunt import treasure_hunt_game

class TestQuestion4(unittest.TestCase):
    def test_secure_transmission(self):
        st = SecureTransmission(6, [[0,2,4],[2,3,1],[2,1,3],[4,5,5]])
        self.assertTrue(st.canTransmit(2, 3, 2))
        self.assertFalse(st.canTransmit(1, 3, 3))
        self.assertTrue(st.canTransmit(2, 0, 3))
        self.assertFalse(st.canTransmit(0, 5, 6))

    def test_treasure_hunt(self):
        Graph = [
            [2, 5],
            [3],
            [0, 4, 5],
            [1, 4, 5],
            [2, 3],
            [0, 2, 3]
        ]
        self.assertEqual(treasure_hunt_game(Graph), 0)

if __name__ == "__main__":
    unittest.main()
