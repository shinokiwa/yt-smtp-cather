"""
メール送信ページ
"""
from flask import Blueprint, render_template, current_app, request
from pydantic import BaseModel

from u_dam.sqlite3 import connect_database
from database.tables.mails import get_mail

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


@bp.route('/mail', methods=['POST'])
def mail_post():
    """
    メール送信
    """
    mail_id = request.form['mail_id']
    mail = get_mail(mail_id)

    # メール送信
    current_app.mailer.send(
        mail['mail_from'],
        mail['mail_to'],
        mail['mail_subject'],
        mail['mail_body']
    )

    return render_template('mail.html')
