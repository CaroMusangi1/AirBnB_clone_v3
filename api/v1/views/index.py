#!/usr/bin/python3
"""Module for endpoint (route) status"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def api_status():
    """

    """
responce = {'status': "OK"}
    return jsonify(responce)
