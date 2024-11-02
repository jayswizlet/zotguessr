import unittest
from decimal import Decimal

#from score import calculate_score
from score import * #Not sure why this isn't importaitng all of the functions from score
# are you running the file OK
# hmm on my end the function doesn't import unless i manually import by function name
# picture_locations doesnt work for me in this case. Its throwing me errors
# I cant run the terminal on my end in the live share
# here i'll commit and push and you can try on your end
# sounds good, ill check it locally

class ScoreTests(unittest.TestCase):
    def test_calculate_score(self):
        self.assertEqual(calculate_score(picture_locations[0], picture_locations[0]), Decimal(0))
        self.assertEqual(calculate_score(picture_locations[0], [0, 0]), Decimal(122.5520269661836))
        self.assertEqual(calculate_score(picture_locations[0], [33.647022811771905, -117.83780073963234]), Decimal(0.004971594462651602))
        self.assertNotEqual(calculate_score(picture_locations[0], [33.647022811771905, -117.83780073963234]), Decimal(0))
    
    def test_picture_coordinates(self):
        self.assertEqual(picture_coordinates(0), picture_locations[0])

if __name__ == "__main__":
    unittest.main()