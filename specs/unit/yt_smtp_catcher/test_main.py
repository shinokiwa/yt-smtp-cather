"""
yt_smtp_catcher/__main__.py のテスト
"""
import pytest
from pytest_mock import MockerFixture

from yt_smtp_catcher.__main__ import *

def test_main(mocker: MockerFixture):
    """
    it:
        - メイン処理を実行する。
    
    expect:
        - 動かしようがないので、インポートエラーが発生しない程度の確認のみを行う。
    """
    pass