# coding: utf-8
from . import main
from flask import render_template, redirect, url_for, request
from app.models import User, Client
from app import db
from .forms import RegisterForm, CRegisterForm
from flask_login import login_required, current_user

# test views
@main.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"


@main.route('/register/', methods=["POST", "GET"])
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


@main.route('/cregister/', methods=["POST", "GET"])
@login_required
def cregister():
    """
    第三方应用注册接口
    """
    form = CRegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        desc = form.desc.data
        client = Client(
            name = name,
            desc = desc,
            dev_id = current_user.id
        )
        db.session.add(client)
        db.session.commit()
        return redirect(url_for("main.manage", id=current_user.id))
    return render_template("main/cregister.html", form=form)


@main.route('/')
def home():
    """
    show client name, key, token info
    for client developer
    """
    developer = current_user
    # clients = developer.clients.all()
    return render_template(
        "main/home.html",
        developer = developer
    )


@main.route('/manage/<int:id>/')
@login_required
def manage(id):
    user = User.query.get_or_404(id)
    clients = user.clients.all()
    for client in clients:
        client.client_token = client.generate_client_token()
    return render_template(
        "main/manage.html",
        clients = clients
    )


@main.route('/delete/', methods=["GET"])
@login_required
def delete():
    client_id = request.args.get("client")
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for("main.manage", id=current_user.id))

