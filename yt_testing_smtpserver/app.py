"""
Flaskのappを作成する
"""
from flask import Flask
from u_dam.sqlite3 import setup_database, connect_database

from .routes import setup_routes

def create_app(db_path=None):
    app = Flask(__name__)

    if db_path is None:
        db_path = '/workspace/data/mail.sqlite3'
    
    setup_database(connect_database, db_path, 'database').close()

    app.config['DB_PATH'] = db_path

    app.register_blueprint(setup_routes())

    return app