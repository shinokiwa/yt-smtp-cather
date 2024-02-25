"""
ルーティング定義
"""
from flask import Blueprint
from importlib import import_module

def setup_blueprint () -> Blueprint:
    """
    ルーティングが設定されたBlueprintを作成する。

    Return:
        Blueprint: ルーティング設定ずみのBlueprint
    """
    bp = Blueprint('routes', __name__)

    bp.register_blueprint(import_module('yt_smtp_catcher.blueprints.index').bp)
    bp.register_blueprint(import_module('yt_smtp_catcher.blueprints.detail').bp)
    bp.register_blueprint(import_module('yt_smtp_catcher.blueprints.mail').bp)
    bp.register_blueprint(import_module('yt_smtp_catcher.blueprints.delete').bp)

    return bp