#!/usr/bin/python3
"""Module for endpoint (route) status"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'])
def status():
    """Endpoint that retrieves the status"""
    result = {"status": "OK"}
    return jsonify(result)

