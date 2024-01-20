"""
転送先の設定テーブル


"""
import sqlite3

def create_table(conn: sqlite3.Connection):
    """
    テーブル作成
    """
    conn.execute((
        "CREATE TABLE IF NOT EXISTS transport_map ("
            "id          INTEGER                 PRIMARY KEY,"              # ID
            "domain      TEXT        NOT NULL,"                             # ドメイン
            "transport   TEXT        NOT NULL,"                             # 転送先
            "registed_at DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP,"# 登録日時
            "updated_at DATETIME     NOT NULL    DEFAULT CURRENT_TIMESTAMP" # 更新日時
        ");"
    ))
    conn.commit()
