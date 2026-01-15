from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
if not API_KEY:
    raise ValueError("WEATHER_API_KEY is not set in .env")

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    # return jsonify(message="Hello from the backend!")

    city = request.args.get("city")
    
    if not city:
        return jsonify({"error": "Please provide a city parameter"}), 400
    
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params, timeout=8)
        response.raise_for_status()
        data = response.json()

        # if response.status_code !=200:
        #     return jsonify({
        #         "error": data.get("message", "City not found.")
        #     }), response.status_code
        
        print(data)
        return jsonify(data)
    except requests.exceptions.HTTPError as e:
        return jsonify({"error": "City not found."}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)