# coding: utf-8

"""
    users.py
    ~~~~~~~~

        muxioauth用户API
"""

import base64
from . import api
from .authentication import auth
from app import db
from app.decorators import grant_required
from app.models import User, Client
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

@api.route('/user/', methods=["PUT"])
@auth.login_required
def update_user():
    token_header = request.headers.get('authorization')
    if token_header:
        json_data = request.get_json(force=True)
        token_hash = token_header[6:]
        token_8 = base64.b64decode(token_hash)
        user_email = token_8.split(":")[0]

        user = User.query.filter_by(email=user_email).first()

        if json_data.has_key('qq'): user.qq = json_data['qq']
        if json_data.has_key('school'): user.school = json_data['school']
        if json_data.has_key('username'): user.username = json_data['username']
        if json_data.has_key('sid'): user.sid = json_data['sid']
        if json_data.has_key('phone'): user.phone = json_data['phone']

        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_json()), 200
    return jsonify(), 401
         

@api.route('/username_exists/', methods=["GET"])
def username_exits():
    """check username exists"""
    username = request.args.get("username")
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({}), 200
    else:
        return jsonify({}), 400


@api.route('/email_exists/', methods=["GET"])
def email_exits():
    """check email exists"""
    email = request.args.get("email")
    user = User.query.filter_by(email=email).first()
    if user is None:
        return jsonify({}), 200
    else:
        return jsonify({}), 400
