from __future__ import absolute_import

from celery import shared_task
import smtplib
import email.utils
from email.mime.text import MIMEText


@shared_task
def send_mail(username):
    # Create the message
    msg = MIMEText('Hello, admin. You have a new user - ' + username)
    msg['To'] = email.utils.formataddr(('Admin', 'admin@admin.com'))
    msg['From'] = email.utils.formataddr(('User', username))
    msg['Subject'] = 'New notification'

    server = smtplib.SMTP('127.0.0.1', 25)
    server.set_debuglevel(False)  # show communication with the server
    try:
        server.sendmail(
            'admin@example.com', ['admin@gmail.com'], msg.as_string())
    finally:
        server.quit()
