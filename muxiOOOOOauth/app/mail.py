# coding: utf-8
from . import mail, app, celery
from flask import render_template
from flask_mail import Message


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
    send_async_email.delay(msg)


# a celery task: send async email
@celery.task(default_retry_delay=30)
def send_async_email(msg):
    with app.app_context():
        """send async email in application context"""
        mail.send(msg)
