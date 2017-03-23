# -*- coding: utf-8 -*-

from . import mail, app, celery
from flask import render_template, jsonify
from flask_mail import Message


def msg_to_dict(to, subject, template, **kwargs):
    """change mail to dict for json seriaization"""
    msg = Message(
        subject=app.config['AUTH_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[to]
    )
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    return msg.__dict__


# send mail
def send_mail(to, subject, template, **kwargs):
    """send mail function"""
    send_async_email.delay(msg_to_dict(to, subject, template, **kwargs))


# a celery task: send async email
@celery.task(default_retry_delay=30)
def send_async_email(msg_dict):
    with app.app_context():
        """send async email in application context"""
        msg = Message()
        msg.__dict__.update(msg_dict)
        mail.send(msg)
