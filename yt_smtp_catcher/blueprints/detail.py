"""
詳細ページ
"""
from flask import Blueprint, render_template, current_app

from u_dam.sqlite3 import connect_database
from database.tables.mails import get_mail

bp = Blueprint('detail', __name__)

@bp.route('/detail/<int:mail_id>')
def detail(mail_id:int):
    """
    詳細ページ
    """
    conn = connect_database(current_app.config['DB_PATH'])
    mail = get_mail(conn, mail_id)
    return render_template('detail.html', mail=mail)
