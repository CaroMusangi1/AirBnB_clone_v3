#!/usr/bin/python3
"""Module for endpoint (route) status"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def api_status():
    """
Returns na JSON responce for RESTful API health.

    """
responce = {'status': "OK"}
    return jsonify(responce)

@app_views.route('/stats')
def get_stats():
    """Endpoint that retrieves the number of each objects by type"""
    result = {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
    return jsonify(result)
