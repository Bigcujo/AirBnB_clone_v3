#!/usr/bin/python3
"""this is the index route"""
from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieves the number of each objects by it's type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)

@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the current status of the API"""
    return jsonify({
        "status": "OK"
        })
