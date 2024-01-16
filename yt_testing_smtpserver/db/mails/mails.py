"""
mailsテーブルの操作モジュール
"""
import sqlite3

def get_all_mails(conn:sqlite3.Connection):
    """全てのメールを取得する

    Args:
        conn (sqlite3.Connection): データベース接続オブジェクト

    Returns:
        List[sqlite3.Row]: メールのリスト
    """
    cur = conn.execute("SELECT * FROM mails ORDER BY updated_at DESC")
    return cur.fetchall()

def delete_mail(conn:sqlite3.Connection, mail_id:int):
    """メールを削除する

    Args:
        conn (sqlite3.Connection): データベース接続オブジェクト
        mail_id (int): メールID
    """
    conn.execute("DELETE FROM mails WHERE id=?", (mail_id,))
    conn.commit()