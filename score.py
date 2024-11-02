from math import sqrt
from decimal import Decimal

# Hardcoded coordinates.  #Are you getting the coordinate data off of google maps? (making sure source is consistent with cooordinate data)
# Key: picture ID
# Value: list of latitude and longitude
picture_coordinates = {
    # Aldrich Park
    0: [33.64649844716821, -117.84274460383592]
}

# @params:
#   coord_pic: list of latitude and longitude representing actual picture location
#   coord_guess: list of latitude and longitude representing user guess location
# Returns:
#   distance between coordinates
def calculate_score(id, coord_guess):
    coord_pic = picture_coordinates[id]
    return sqrt((Decimal(coord_pic[1]) - Decimal(coord_guess[1])) ** 2 + (Decimal(coord_pic[0]) - Decimal(coord_guess[0])) ** 2)
