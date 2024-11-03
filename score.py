from math import sqrt
from decimal import Decimal
from prompt import getCordsByID
# @params:
#   coord_pic: list of latitude and longitude representing actual picture location
#   coord_guess: list of latitude and longitude representing user guess location
# Returns:
#   distance between coordinates


def calculate_score(paramID, coord_guess):
    # Retrieve coordinates using getCordsByID
    coord_pic = getCordsByID(paramID)
    
    if not coord_pic:
        print(f"No coordinates found for ID {paramID}")
        return None  # or return a specific value indicating an error

    # Calculate score using coordinates
    return Decimal(sqrt((Decimal(coord_pic["longitude"]) - Decimal(coord_guess["longitude"])) ** 2 + 
                        (Decimal(coord_pic["latitude"]) - Decimal(coord_guess["latitude"])) ** 2))


# sample_id = 1
# guess_coords = (34.0522, -118.2437)  # Random Cord Guess

# score = calculate_score(sample_id, guess_coords)
# if score is not None:
#     print("Score:", score)
# else:
#     print("Could not calculate score due to missing coordinates.")