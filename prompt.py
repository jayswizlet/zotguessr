import requests
import json

from supabase_py import create_client

import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

supabase_url = 'https://zkbauuiquqlwlibhhuoy.supabase.co'
supabase_key = os.getenv("KEY")
supabase = create_client(supabase_url, supabase_key)


def prompt_image(id):
    response = supabase.table('locations').select("url").eq("id", str(id)).execute()
    #print(response)
    return response["data"][0]["url"]

import random
numImages = 3
numRows = 5
def prompt_images():
    images = []
    ids = [-1]
    for i in range(numImages):
        if(len(ids) - 1 == numRows):
            break
        id = -1
        while(id in ids):
            id = random.randint(0, numRows - 1)
        images.append({ "id": id, "url": prompt_image(id) })
        ids.append(id)
    return images



def getByIDHelper(paramID):
    try:
        # Replace "table" with the actual name of your table, e.g., "locations"
        response = supabase.table("locations").select("url, latitude, longitude").eq("id", str(paramID)).execute()
        
        # Check and print the response to confirm data structure
        print("Full response from Supabase:", response)

        if "data" in response and response["data"]:
            return response["data"][0]
        
        print("No data found for the given ID:", paramID)
        return None

    except Exception as e:
        print("Exception occurred while fetching data:", e)
        return None


def getPhotoByID(paramID):
    data = getByIDHelper(paramID)
    
    # Check if data is not None and contains expected field "photoURL"
    if data:
        print("Retrieved data:", data)  # Debugging print
        # Dynamically check if "photoURL" or "url" exists in the data
        photo_url = data.get("photoURL") or data.get("url")
        
        if photo_url:
            return {"photoURL": photo_url}
        
        print("Expected photo URL field ('photoURL' or 'url') not found in data.")
    return None

def getCordsByID(paramID):
    data = getByIDHelper(paramID)
    if data:
        return {"latitude": data["latitude"], "longitude": data["longitude"]}
    return None




# Function to scrape cords and photo from given ID
# sample_id = 1  # Replace with an existing ID in your table

# # Test getPhotoByID function
# photo_data = getPhotoByID(sample_id)
# print("Photo Data:", photo_data)

# # Test getCordsByID function
# cords_data = getCordsByID(sample_id)
# print("Coordinates Data:", cords_data)
