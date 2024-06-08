#!/usr/bin/python3
"""
Main module for running the HBNB API.
"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask


app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST') or '0.0.0.0'
    port = int(os.getenv('HBNB_API_PORT') or 5000)
    app.run(host=host, port=port, threaded=True)
