"""
DB接続ユーティリティ
"""
import os

def get_environ (key) -> str:
    """
    必須環境変数を取得する。

    Args:
        key (str): 環境変数名
    
    Returns:
        str: 環境変数の値

    Raises:
        RuntimeError: 環境変数が設定されていない
    """
    try:
        return os.environ[key]
    except KeyError:
        raise RuntimeError(f'環境変数 {key} が設定されていません。')

def get_database_path() -> str:
    """
    DBファイルのパスを取得する。
    DBファイルのパスは環境変数 YT_TSSERVER_DB_PATH から取得する。

    Returns:
        str: DBファイルのパス

    Raises:
        RuntimeError: 環境変数 YT_TSSERVER_DB_PATH が設定されていない
    """
    return get_environ('YT_TSSERVER_DB_PATH')

def get_sqllite_path() -> str:
    """
    SQLite3のセットアップSQLファイルのパスを取得する。
    SQLite3のセットアップSQLファイルのパスは環境変数 YT_TSSERVER_SQLITE_PATH から取得する。

    Returns:
        str: SQLite3のセットアップSQLファイルのパス
        
    Raises:
        RuntimeError: 環境変数 YT_TSSERVER_SQLITE_PATH が設定されていない
    """
    return get_environ('YT_TSSERVER_SQLITE_PATH')