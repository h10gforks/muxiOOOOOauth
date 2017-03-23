# -*- coding: utf-8 -*-

import random
from flask import request, jsonify
from app import db
from . import api
from app.models import User
from app.mail import send_mail


@api.route('/forgot_password/get_captcha/', methods=['POST'])
def get_captcha():
    """
    获取邮箱验证码
    """
    username = request.json.get('username') or "同学"
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({}), 404
    captcha = '%04d' % random.randrange(0, 9999)
    send_mail(email, '木犀通行证验证码', 'mail/reset', username=username, captcha=captcha)
    user.reset_t = user.generate_reset_token(captcha)
    return jsonify({}), 200


@api.route('/forgot_password/reset/', methods=['POST'])
def reset():
    """重置密码"""
    captcha = request.json.get('captcha')
    email = request.json.get('email')
    new_password = request.json.get('new_password')
    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({}), 404

    try:
        tid, tcaptcha = User.verify_reset_token(user.reset_t)
    except TypeError:
        return jsonify({}), 403
    if tid != user.id or int(tcaptcha) != int(captcha):
        return jsonify({}), 403

    user.password = new_password
    db.session.add(user)
    db.session.commit()

    return jsonify({}), 200
