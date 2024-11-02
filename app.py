from flask import Flask, request, jsonify
import os
app = Flask(__name__)
from score import *

#Baseline Code
@app.route("/")
def home():
    return "Flask Home Page"

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "YOUR_GOOGLE_MAPS_API_KEY")

@app.route("/getcode", methods=['GET'])
def geoData():

    address = request.args.get("address")
    if not address:
        return jsonify({"error": "Please provide an address"}), 400

    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Request to Google Maps API failed"}), 500

    # Check if the API returned results
    if "results" not in data or not data["results"]:
        return jsonify({"error": "No results found"}), 404

    data = request.json()
    location = data["results"][0]["geometry"]["location"]
    address = request.args.get("address")
    return jsonify({
        "address": address,
        "latitude": location["lat"],
        "longitude": location["lng"]
    })




if __name__ == "__main__":
    app.run(debug=True)

