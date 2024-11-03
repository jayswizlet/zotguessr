from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

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
    #Extract location data/API Call
    data = request.args
    #print(type(calculate_score(int(data["prompt_id"]), [Decimal(data["latitude"]), Decimal(data["longitude"])])))
    return {
        # Decimal(1) / ...
        "score": float(Decimal(1) / calculate_score(int(data["prompt_id"]), [Decimal(data["latitude"]), Decimal(data["longitude"])]))
    }

# response looks like this:
# [https://zkbauuiquqlwlibhhuoy.supabase.co/storage/v1/object/public/location-images/Aldrich-Park_1600.jpg,
# ...,
# ...]
@app.route("/getPrompt", methods=['GET', 'POST'])
@cross_origin()
def get_prompt():
    return jsonify(prompt_images())

if __name__ == "__main__":
    app.run(debug=True)

