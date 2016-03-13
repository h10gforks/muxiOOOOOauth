# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Required


class RegisterForm(Form):
    """开发者注册表单"""
    username = StringField(validators=[Required()])
    password = PasswordField(validators=[Required()])
    email = StringField(validators=[Required()])
    submit = SubmitField('submit')


class CRegisterForm(Form):
    """第三方应用注册表单"""
    name = StringField(validators=[Required()])
    desc = TextAreaField(validators=[Required()])
    submit = SubmitField('submit')

