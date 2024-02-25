"""
yt_smtp_catcher/app.py のテスト
"""
import pytest
from pytest_mock import MockerFixture

from flask import Flask

from yt_smtp_catcher.app import *

def test_create_app(mocker: MockerFixture):
    """
    create_app

    it:
        - Flaskアプリケーションを作成する。
    
    expect:
        - setup_database が呼び出されること。
        - Blueprint が登録されること。
        - Flaskアプリケーションが返されること。
    """
    mock_setup_database = mocker.patch('yt_smtp_catcher.app.setup_database')
    mock_setup_blueprint = mocker.patch('yt_smtp_catcher.app.setup_blueprint')

    app = create_app()

    assert type(app) == Flask
    assert app.config['DB_PATH'] == '/workspace/data/mail.sqlite3'
    assert mock_setup_database.call_count == 1
    assert mock_setup_blueprint.call_count == 1
