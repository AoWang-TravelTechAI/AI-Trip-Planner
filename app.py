import openai
import googlemaps
import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

app = Flask(__name__)

def generate_itinerary(destination, days):
    prompt = f"Create a {days}-day travel itinerary for {destination}. Include sightseeing, food, and activities for each day."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional travel planner."},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"]

def get_real_time_attractions(destination):
    result = gmaps.places(query=f"top attractions in {destination}")
    attractions = [place["name"] for place in result.get("results", [])[:5]]
    return attractions

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/plan_trip", methods=["POST"])
def plan_trip():
    data = request.get_json()
    destination = data.get("destination")
    days = int(data.get("days"))

    itinerary_text = generate_itinerary(destination, days)
    itinerary_list = itinerary_text.strip().split("\n")

    attractions = get_real_time_attractions(destination)

    return jsonify({
        "destination": destination,
        "itinerary": itinerary_list,
        "attractions": attractions
    })

if __name__ == "__main__":
    app.run(debug=True)

