-- 論理名: メール保存テーブル

-- 受信したメールを保存するテーブル。
-- 保存作業はPostfixが実行する。

CREATE TABLE IF NOT EXISTS mails (

    id          INTEGER                 PRIMARY KEY,                -- ID
    sender      TEXT        NOT NULL,                               -- 送信者
    recipient   TEXT        NOT NULL,                               -- 受信者
    subject     TEXT        NOT NULL,                               -- 件名
    mail_data   TEXT        NOT NULL,                               -- メールデータ
    registed_at DATETIME    NOT NULL    DEFAULT CURRENT_TIMESTAMP,  -- 登録日時
    updated_at DATETIME     NOT NULL    DEFAULT CURRENT_TIMESTAMP   -- 更新日時
);