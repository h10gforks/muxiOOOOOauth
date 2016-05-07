# coding: utf-8

from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login!')


class LostForm(Form):
    email = StringField('email', validators=[DataRequired()])
    newpassword = PasswordField('newpassword', validators=[DataRequired()])
    submit = SubmitField('submit')
