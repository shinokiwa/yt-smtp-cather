"""
メール削除
"""
from flask import Blueprint, current_app, redirect

from u_dam.sqlite3 import connect_database
from database.tables.mails import delete_mail, delete_mail_all

bp = Blueprint('delete', __name__)

@bp.route('/delete_all')
def delete_all():
    """
    メール削除
    """
    conn = connect_database(current_app.config['DB_PATH'])
    delete_mail_all(conn)
    return redirect('/')

@bp.route('/delete/<int:mail_id>')
def delete(mail_id:int):
    """
    メール削除
    """
    conn = connect_database(current_app.config['DB_PATH'])
    delete_mail(conn, mail_id)
    return redirect('/')
