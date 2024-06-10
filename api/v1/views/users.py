#!/usr/bin/python3
"""Handles all default RESTFul API actions for User objects"""
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a specific User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a User"""
    data_dict = request.get_json()
    if not data_dict:
        abort(400, description="Not a JSON")

    if 'email' not in data_dict:
        abort(400, description="Missing email")
    if 'password' not in data_dict:
        abort(400, description="Missing password")

    new_user = User(**data_dict)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Updates a User"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    data_dict = request.get_json()
    if not data_dict:
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data_dict.items():
        if key not in ignore:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
