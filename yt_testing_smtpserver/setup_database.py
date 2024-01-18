"""
DBセットアップスクリプト

/workspace/sqlite/*.sql を一通り実行する。
"""
import logging; logger = logging.getLogger(__name__)
import os

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

    file_list = os.listdir(sql_dir)
    file_list.sort()

    for sql_file in file_list:
        if not sql_file.endswith('.sql'):
            continue
        with open(os.path.join(sql_dir, sql_file)) as f:
            db.executescript(f.read())
            logger.info('Executed: %s', sql_file)

    db.commit()
    db.close()

if __name__ == '__main__':
    setup_database()