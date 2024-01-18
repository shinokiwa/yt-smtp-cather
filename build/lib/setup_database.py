"""
DBセットアップスクリプト

/workspace/sqlite/*.sql を一通り実行する。
"""
import os
import sqlite3

from .db import (
    connect_database,
    get_database_path,
    get_sqllite_path
)

def setup_database():
    """
    DBセットアップ
    """
    db_path = get_database_path()
    sql_dir = get_sqllite_path()

    db = connect_database(db_path)

    file_list = os.listdir(sql_dir).sort()

    for sql_file in file_list:
        if not sql_file.endswith('.sql'):
            continue
        with open(os.path.join(sql_dir, sql_file)) as f:
            db.executescript(f.read())

    db.commit()
    db.close()

if __name__ == '__main__':
    setup_database()