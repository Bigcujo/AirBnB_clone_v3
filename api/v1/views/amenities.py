#!/usr/bin/python3
""" create the ammenty metho """
import models
from flask import jsonify, request, abort
from models.amenity import Amenity
from api.v1.views import app_views


@app_views.route('/amenities', methods=['GET'])
def get_all_amenities():
    """get all the amenities available"""
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])

   
@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Retrieves the given id Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes the given ID  Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """Creates an Amenity"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    amenity = Amenity(**data)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """Updates an Amenity object by the given id"""
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    storage.save()
    return jsonify(amenity.to_dict()), 200

