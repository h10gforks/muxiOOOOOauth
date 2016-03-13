# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class RegisterForm(Form):
    """开发者注册表单"""
    username = StringField(validators=[Required()])
    password = StringField(validators=[Required()])
    email = StringField(validators=[Required()])
    submit = SubmitField('submit')


class CRegisterForm(Form):
    """第三方应用注册表单"""
    name = StringField(validators=[Required()])
    client_key = StringField(validators=[Required()])
    submit = SubmitField('submit')

