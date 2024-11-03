import unittest
from decimal import Decimal

from score import * 
class ScoreTests(unittest.TestCase):
    def test_calculate_score(self):
        #print(type(calculate_score(0, [1, 2])))
        self.assertEqual(calculate_score(0, picture_coordinates[0]), Decimal(0))
        self.assertEqual(calculate_score(0, [0, 0]), Decimal(122.5520269661836))
        self.assertEqual(calculate_score(0, [33.647022811771905, -117.83780073963234]), Decimal(0.004971594462651602))
        self.assertNotEqual(calculate_score(0, [33.647022811771905, -117.83780073963234]), Decimal(0))

if __name__ == "__main__":
    unittest.main()
