import sys
import sqlite3
from email.parser import Parser
from email.header import decode_header, make_header

def save_mail_to_db(sender, recipients, mail_data):
    """
    メールをデータベースに保存する

    Parameters:
        sender (str): 送信元メールアドレス
        recipients (str): 受信先メールアドレス
        mail_data (str): メールデータ
    """
    # メールデータをパース
    parser = Parser()
    mail = parser.parsestr(mail_data)

    # 件名をデコード
    if 'Subject' in mail:
        subject = mail['Subject']
        subject = make_header(decode_header(subject))
        subject = str(subject)
    else:
        subject = '(no subject)'

    # SQLiteデータベースに接続
    conn = sqlite3.connect('/workspace/data/mail.sqlite3')
    cursor = conn.cursor()

    # メールをデータベースに保存するクエリ
    cursor.execute(
        "INSERT INTO mails (sender, recipient, subject, mail_data) VALUES (?, ?, ?, ?)",
        (sender, recipients, subject, mail_data))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Postfixからメールデータを受け取る
    sender = sys.argv[1]
    recipients = sys.argv[2]
    mail_data = sys.stdin.read()

    # データベースに保存
    save_mail_to_db(sender, recipients, mail_data)
