from flask import Flask, request, jsonify
app = Flask(__name__)

from decimal import Decimal
from score import calculate_score

#Baseline Code
@app.route("/")
def home():
    return "Flask Home Page"

@app.route("/score", methods=['GET'])
def score():
    #Extract location data/API Call
    data = request.args
    return jsonify({
        "score": calculate_score(int(data["prompt_id"]), [Decimal(data["latitude"]), Decimal(data["longitude"])])
    })

if __name__ == "__main__":
    app.run(debug=True)

