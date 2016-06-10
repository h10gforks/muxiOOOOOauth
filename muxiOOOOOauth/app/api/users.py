# coding: utf-8

"""
    users.py
    ~~~~~~~~

        muxioauth用户API
"""

import json
from . import api
from .authentication import auth
from app.decorators import grant_required
from app.models import User
from flask import jsonify, request


@api.route('/users/<int:id>/', methods=["GET"])
@grant_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json()), 200


@api.route('/users/', methods=["GET", "POST"])
@grant_required
def create_user():
    user = User.from_json(request.get_json())
    return jsonify({
            "created": user.id
    }), 201


@api.route('/user/', methods=["GET"])
def get_email_user():
    email = request.args.get('email')
    if email:
        user = User.query.filter_by(email=email).first()
    else:
        user = User.query.first()
    return jsonify(user.to_json()), 200
