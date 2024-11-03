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
    print(response)
    return response["data"][0]

import random
numImages = 3
numRows = 1
def prompt_images():
    images = []
    ids = [-1]
    for i in range(numImages):
        if(len(ids) - 1 == numRows):
            break
        id = -1
        while(id in ids):
            id = random.randint(0, numRows - 1)
        images.append(prompt_image(id))
        ids.append(id)
    return images



