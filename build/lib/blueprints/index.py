"""
ルートアクセス時の処理を記述する
"""
from flask import Blueprint, render_template, current_app

from yt_testing_smtpserver.db import connect_database
from yt_testing_smtpserver.db.mails import get_all_mails

bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    """
    ルートアクセス時の処理
    """
    conn = connect_database(current_app.config['DB_PATH'])
    mails = get_all_mails(conn)
    return render_template('index.html', mails=mails)