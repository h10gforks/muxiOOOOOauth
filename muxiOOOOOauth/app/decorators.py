# coding: utf-8

"""
    decorators.py
    ~~~~~~~~~~~~~

        muxioauth 装饰器
"""

from .models import Client, User
from functools import wraps
from flask import request, g, abort
import base64


# 第三方应用授权装饰器
def grant_required(f):
    # "Basic Base64("grant token:")"
    @wraps(f)
    def decorated(*args, **kwargs):
        token_header = request.headers.get('authorization', None)
        if token_header:
            token_hash = token_header[6:]
            token_8 = base64.b64decode(token_hash)
            token = token_8[:-1]
            if not Client.verify_client_token(token):
                abort(403)
            else:
                g.client = Client.verify_client_token(token)
            return f(*args, **kwargs)
    return decorated


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('authorization')
        token_header = request.headers.get('token')

        if token_header:
            uid = User.verify_login_token(token_header)
            if not uid:
                abort(401)
        elif auth_header:
            json_data = request.get_json(force=True)
            auth_encoded = auth_header[6:]
            auth_decoded = base64.b64decode(auth_encoded)
            email_passwd = auth_decoded.split(":")
            user_email = email_passwd[0]
            user_passwd = email_passwd[1]
            u = User.query.filter_by(email=user_email).first()
            if not u.verify_password(user_passwd):
                abort(401)
        else:
            abort(401)
        return f(*args, **kwargs)
    return decorated
