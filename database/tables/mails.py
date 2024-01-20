"""
メール保存テーブル

- 受信したメールを保存するテーブル。
- 保存作業はPostfixが実行する。
"""
import sqlite3


def create_table(conn: sqlite3.Connection):
    """
    テーブル作成
    """
    conn.execute((
        "CREATE TABLE IF NOT EXISTS mails ("
            "id          INTEGER                 PRIMARY KEY,"              # ID
            "sender      TEXT        NOT NULL,"                             # 送信者
            "recipient   TEXT        NOT NULL,"                             # 受信者
            "subject     TEXT        NOT NULL,"                             # 件名
            "mail_data   TEXT        NOT NULL,"                             # メールデータ
            "registed_at DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP,"# 登録日時
            "updated_at DATETIME     NOT NULL    DEFAULT CURRENT_TIMESTAMP" # 更新日時
        ");"
    ))
    conn.commit()


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