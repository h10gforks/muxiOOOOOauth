# coding: utf-8

"""
    decorators.py
    ~~~~~~~~~~~~~

        muxioauth 装饰器
"""

from .models import Client
from functools import wraps
from flask import request, g
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

