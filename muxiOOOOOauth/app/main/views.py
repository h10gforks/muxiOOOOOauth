# coding: utf-8
from . import main
from flask import render_template, redirect, url_for
from app.models import User, Client
from app import db
from .forms import RegisterForm, CRegisterForm
from flask_login import login_required, current_user

# test views
@main.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"


@main.route('/register/')
def register():
    """
    开发者账号注册接口
    """
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        user = User(
            username = username,
            password = password,
            email = email
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("main/register.html", form=form)


@main.route('/cregister/')
@login_required
def cregister():
    """
    第三方应用注册接口
    """
    form = CRegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        client_key = form.client_key.data
        client = Client(
            name = name,
            client_key = client_key,
            dev_id = current_user.id
        )
        db.session.add(client)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("cregister.html", form=form)


@main.route('/')
@login_required
def home():
    """
    show client name, key, token info
    for client developer
    """
    developer = current_user
    clients = developer.clients.all()
    return render_template(
        "home.html",
        developer = developer,
        clients = clients
    )

