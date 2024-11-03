from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from score import calculate_score
from prompt import getCordsByID
import logging 

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from decimal import Decimal
from score import calculate_score
from prompt import prompt_image, prompt_images

#Baseline Code
@app.route("/")
def home():
    return "Flask Home Page"

@app.route("/score", methods=['GET', 'POST'])
@cross_origin()
def score():
    prompt_id = request.args.get("prompt_id")
    longitude = float(request.args.get("longitude"))
    latitude = float(request.args.get("latitude"))
    actualCords = getCordsByID(prompt_id)
    response = {
        "score": float(Decimal(1) / calculate_score(prompt_id, {"longitude": longitude, "latitude": latitude})),
        "longitude": float(actualCords["longitude"]),
        "latitude": float(actualCords["latitude"])
    }
    return response


# response looks like this:
# [https://zkbauuiquqlwlibhhuoy.supabase.co/storage/v1/object/public/location-images/Aldrich-Park_1600.jpg,
# ...,
# ...]
@app.route("/getPrompts", methods=['GET', 'POST'])
@cross_origin()
def get_prompt():
    return prompt_images()


if __name__ == "__main__":
    app.run(debug=True, port=3001)

