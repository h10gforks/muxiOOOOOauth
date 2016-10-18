# coding: utf-8

from app import db
from . import auth
from flask import render_template, url_for, redirect, flash, session, request
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User
from .forms import LoginForm, LostForm
from app.mail import send_mail
import base64


@auth.route('/login/', methods=['POST', 'GET'])
def login():
    """
    同步登录muxiOOOOOauth
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if user is not None and \
            user.verify_password(password):
                login_user(user)
                return redirect("http://xueer.muxixyz.com/privateship/?email=%s" % email)
    return render_template('auth/login.html')


@auth.route('/register/', methods=['POST', 'GET'])
def register():
    """
    同步注册
    """
    if request.method == 'POST':
        email  = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(
                email = email,
                username = username,
                password = password,
                role_id = 3
            )
            db.session.add(user)
            db.session.commit()
    return render_template('auth/register.html')


@auth.route('/lostfound/', methods=['POST', 'GET'])
def lostfound():
    """
    设置新密码界面
    点击确认, 发送确认邮件
    确认邮件防止别人修改已知邮箱密码
    """
    form = LostForm()
    if form.validate_on_submit():
        email = form.email.data
        newpassword = form.newpassword.data
        user = User.query.filter_by(email = email).first()
        if user:
            # session[str(user.id)] = newpassword
            token = user.generate_confirm_token()
            send_mail(
                email, 'Confirm a New Password', 'auth/confirm',
                user=user, token=token,
                neo1218=base64.b64encode(newpassword)
            )
        else:
            return False
    return render_template('auth/lost.html', form=form)


@auth.route('/confirm/<token>/')
def confirm(token):
    """
    确认密码是用户本人修改
    """
    id = User.verify_confirm_token(token)
    user = User.query.get_or_404(id)
    if user:
        user.password = base64.b64decode(request.args.get('neo1218'))
        db.session.add(user)
        db.session.commit()
    else:
        return False
    newpassword = base64.b64decode(request.args.get('neo1218'))
    return render_template('auth/success.html', newpassword=newpassword)
