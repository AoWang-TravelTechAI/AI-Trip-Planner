import os
import requests
import googlemaps
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GOOGLE_MAPS_API_KEY")

# Initialize Google Maps client
gmaps = googlemaps.Client(key=google_api_key)

# Initialize Flask app
app = Flask(__name__)

# Function to generate travel itinerary using Groq (LLaMA model)
def generate_itinerary(destination, days):
    prompt = f"Please create a {days}-day travel itinerary for {destination}, including sightseeing, food, and activity suggestions for each day."

    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.3-70b-versatile",  # Updated to supported model
        "messages": [
            {"role": "system", "content": "You are a professional travel planner."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        print("Error in generate_itinerary:", e)
        return "Error generating itinerary."

# Function to get top 5 attractions using Google Maps Places API
def get_real_time_attractions(destination):
    try:
        result = gmaps.places(query=f"top attractions in {destination}")
        attractions = [place["name"] for place in result.get("results", [])[:5]]
        return attractions
    except Exception as e:
        print("Error in get_real_time_attractions:", e)
        return ["Attraction data unavailable"]

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Trip planning route
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

# Run the app
if __name__ == "__main__":
    print("Registered routes:")
    print(app.url_map)

    app.run(debug=True)


