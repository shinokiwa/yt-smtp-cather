import sqlite3
import sys

def save_mail_to_db(sender, recipients, mail_data):
    # SQLiteデータベースに接続
    conn = sqlite3.connect('/workspace/data/mail.sqlite3')
    cursor = conn.cursor()

    # メールをデータベースに保存するクエリ
    # ここでは単純化のため、実際のテーブル構造やデータ保存方法によって変更が必要です
    cursor.execute(
        "INSERT INTO mails (sender, recipient, subject, mail_data) VALUES (?, ?, '', ?)",
        (sender, recipients, mail_data))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Postfixからメールデータを受け取る
    sender = sys.argv[1]
    recipients = sys.argv[2]
    mail_data = sys.stdin.read()

    # データベースに保存
    save_mail_to_db(sender, recipients, mail_data)
