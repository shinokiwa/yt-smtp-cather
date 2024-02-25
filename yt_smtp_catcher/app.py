"""
Flaskのappを作成する
"""
import os
from flask import Flask
from u_dam.sqlite3 import setup_database, connect_database

from .routes import setup_blueprint

def create_app(db_path=None) -> Flask:
    """
    Flaskのappを作成する。

    Parameters:
        db_path (str): SQLite3データベースファイルのパス

    Returns:
        Flask: Flaskのapp
    """
    app = Flask(__name__)

    if db_path is None:
        db_path = '/workspace/data/mail.sqlite3'
    
    setup_database(connect_database, db_path, 'database').close()

    app.config['DB_PATH'] = db_path

    app.register_blueprint(setup_blueprint())
    app.static_url_path = '/static'
    app.static_folder = os.path.join(os.path.dirname(__file__), 'static')

    return app