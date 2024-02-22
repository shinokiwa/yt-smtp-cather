"""
メール送信ページ
"""
from flask import Blueprint, render_template, current_app
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
    from: str
    to: str
    subject: str


@bp.route('/mail', methods=['POST'])
def mail_post():
    """
    メール送信
    """
    mail_id = request.form['mail_id']
    mail = get_mail(mail_id)

    # メール送信
    current_app.mailer.send(
        mail['from'],
        mail['to'],
        mail['subject'],
        mail['body']
    )

    return render_template('mail.html')
