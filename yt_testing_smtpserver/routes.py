"""
ルーティング定義
"""
from flask import Blueprint
from importlib import import_module

def setup_routes () -> Blueprint:
    """
    ルーティングを設定する
    """
    bp = Blueprint('routes', __name__)

    bp.register_blueprint(import_module('yt_testing_smtpserver.blueprints.index').bp)
    bp.register_blueprint(import_module('yt_testing_smtpserver.blueprints.detail').bp)
    bp.register_blueprint(import_module('yt_testing_smtpserver.blueprints.delete').bp)

    return bp