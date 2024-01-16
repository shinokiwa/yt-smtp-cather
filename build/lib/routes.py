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


    return bp