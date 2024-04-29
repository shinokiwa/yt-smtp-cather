"""
yt_smtp_catcher/routes.py のテスト
"""
import pytest
from pytest_mock import MockerFixture

from flask import Blueprint

from yt_smtp_catcher.routes import *

def test_setup_blueprint(mocker: MockerFixture):
    """
    setup_blueprint

    it:
        - ルーティングが設定されたBlueprintを作成する。
    
    expect:
        - このテストでは単にエラーが発生しない程度の確認のみを行う。
    """

    bp = setup_blueprint()

    assert type(bp) == Blueprint
