import json
from flask import Blueprint, jsonify, request
from shapely.geometry import shape, Point

app = Blueprint("triangulate", __name__)

with open("./app/data/romania-detailed-boundary_1011.geojson", "r") as f:
    js = json.load(f)


@app.route("/triangulate", methods=["GET"])
def get_items():
    query_lat = request.args.get("latitude")
    query_lon = request.args.get("longitude")

    if query_lon and query_lat:
        lat = float(query_lat)
        lon = float(query_lon)

        first_feature = js["features"][0]
        geometry = shape(first_feature["geometry"])
        is_within_polygon = geometry.contains(Point(lat, lon))
        return jsonify(is_within_polygon)
    else:
        return jsonify("Could not triangulate!")
