from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home route to render the frontend
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to generate a simple travel itinerary
@app.route('/plan_trip', methods=['POST'])
def plan_trip():
    data = request.json
    destination = data.get('destination', 'Unknown location')
    days = int(data.get('days', 3))  # Default to 3 days

    itinerary = []
    for i in range(1, days + 1):
        itinerary.append(f"Day {i}: Explore top attractions in {destination}")

    return jsonify({"destination": destination, "itinerary": itinerary})

if __name__ == '__main__':
    app.run(debug=True)
