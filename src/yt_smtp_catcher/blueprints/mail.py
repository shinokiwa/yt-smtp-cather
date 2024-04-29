"""
メール送信ページ
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 

from flask import Blueprint, render_template, current_app, request
from pydantic import BaseModel, ValidationError

bp = Blueprint('mail', __name__)

@bp.route('/mail', methods=['GET'])
def mail():
    """
    詳細ページ
    """
    return render_template('mail.html')

class MailPost(BaseModel):
    mail_from: str
    mail_to: str
    mail_subject: str
    mail_body: str


@bp.route('/mail', methods=['POST'])
def mail_post():
    """
    メール送信
    """
    try:
        mail = MailPost(
            **request.form.to_dict()
        )
    except ValidationError as e:
        return render_template('mail.html', error=True, error_message=e.json(), **request.form.to_dict())

    msg = MIMEMultipart()
    msg['From'] = request.form['mail_from']
    msg['To'] = request.form['mail_to']
    msg['Subject'] = request.form['mail_subject']
    msg.attach(MIMEText(request.form['mail_body'], 'plain'))

    # SMTPサーバに接続
    smtp = smtplib.SMTP('localhost', 25)
    smtp.send_message(msg)
    smtp.quit()

    return render_template('mail.html', result=True, **request.form.to_dict())
