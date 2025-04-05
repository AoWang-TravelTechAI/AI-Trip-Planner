import openai
import googlemaps
import os
from flask import Flask, request, render_template
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Retrieve API keys from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

app = Flask(__name__)

def generate_itinerary(destination, days):
    """
    Generate a travel itinerary using OpenAI's GPT model.
    
    Parameters:
        destination (str): The travel destination.
        days (int): Number of days for the itinerary.
    
    Returns:
        str: The generated itinerary.
    """
    prompt = f"Please create a {days}-day itinerary for {destination}, including sightseeing, food, and activity suggestions for each day."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional travel planner."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response["choices"][0]["message"]["content"]

def get_real_time_attractions(destination):
    """
    Fetch real-time top attractions using Google Maps API.
    
    Parameters:
        destination (str): The travel destination.
    
    Returns:
        list: A list of top attractions.
    """
    places_result = gmaps.places(query=f"top attractions in {destination}")
    attractions = [place["name"] for place in places_result.get("results", [])[:5]]
    return attractions

@app.route("/", methods=["GET", "POST"])
def home():
    """
    Handle the main webpage for travel itinerary generation.
    
    If the user submits a destination and days, it generates an itinerary
    and fetches top attractions.
    
    Returns:
        str: Rendered HTML template with itinerary and attractions.
    """
    itinerary = ""
    attractions = []
    if request.method == "POST":
        destination = request.form["destination"]
        days = request.form["days"]
        itinerary = generate_itinerary(destination, days)
        attractions = get_real_time_attractions(destination)

    return render_template("index.html", itinerary=itinerary, attractions=attractions)

from flask import jsonify  # 确保这一行在顶部导入了

@app.route("/plan_trip", methods=["POST"])
def plan_trip():
    data = request.get_json()
    destination = data.get("destination")
    days = int(data.get("days"))

    itinerary_text = generate_itinerary(destination, days)
    itinerary_list = itinerary_text.strip().split("\n")  # 分成每日行程
    return jsonify({"destination": destination, "itinerary": itinerary_list})

if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
