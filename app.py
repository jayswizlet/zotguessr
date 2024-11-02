from flask import Flask, request, jsonify
app = Flask(__name__)

#Baseline Code
@app.route("/")
def home():
    return "Flask Home Page"

@app.route("/getcode", methods=['GET'])
def geoData():
    #Extract location data/API Call
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

