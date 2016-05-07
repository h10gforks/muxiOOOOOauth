# coding: utf-8
from . import mail, app
from flask import render_template
from flask.ext.mail import Message


# send mail
def send_mail(to, subject, template, **kwargs):
    """
    send mail function
    """
    msg = Message(
        app.config['AUTH_MAIL_SUBJECT_PREFIX'] + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
