# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# CORS(app)

# # 🔑 PUT YOUR GOOGLE API KEY HERE
# API_KEY = "AIzaSyA9LSRfwJw6J4Lx69ZCD9ersMiCR8HEHeA"


# # -------- EMISSION CALCULATION --------
# def calculate_emission(distance_km, duration_min):
#     base = distance_km * 0.2
#     traffic_penalty = duration_min * 0.05
#     return round(base + traffic_penalty, 2)


# # -------- GET ROUTES --------
# def get_routes(source, destination):
#     url = "https://maps.googleapis.com/maps/api/directions/json"

#     params = {
#         "origin": source,
#         "destination": destination,
#         "alternatives": "true",
#         "departure_time": "now",
#         "key": API_KEY
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     if data["status"] != "OK":
#         print("Google Error:", data)
#         return []

#     routes = []

#     for i, route in enumerate(data["routes"]):
#         leg = route["legs"][0]

#         distance_km = leg["distance"]["value"] / 1000
#         duration_min = leg.get("duration_in_traffic", leg["duration"])["value"] / 60

#         emission = calculate_emission(distance_km, duration_min)

#         routes.append({
#             "name": f"Route {chr(65+i)}",
#             "distance": round(distance_km, 2),
#             "duration": round(duration_min, 2),
#             "emission": emission,
#             "polyline": route["overview_polyline"]["points"]
#         })

#     return routes


# # -------- API --------
# @app.route("/get-routes", methods=["POST"])
# def get_routes_api():
#     data = request.json
#     source = data.get("source")
#     destination = data.get("destination")

#     routes = get_routes(source, destination)

#     if not routes:
#         return jsonify({"error": "API failed or invalid location"}), 400

#     best = min(routes, key=lambda x: x["emission"])

#     return jsonify({
#         "routes": routes,
#         "best": best
#     })


# if __name__ == "__main__":
#     app.run(debug=True)