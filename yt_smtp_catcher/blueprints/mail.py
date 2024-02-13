"""
メール送信ページ
"""
from flask import Blueprint, render_template, current_app

from u_dam.sqlite3 import connect_database
from database.tables.mails import get_mail

bp = Blueprint('mail', __name__)

@bp.route('/mail', methods=['GET'])
def mail():
    """
    詳細ページ
    """
    return render_template('mail.html')

