DROP TABLE IF EXISTS mails;

CREATE TABLE mails (
    id INTEGER PRIMARY KEY,
    sender TEXT NOT NULL,
    recipient TEXT NOT NULL,
    subject TEXT NOT NULL,
    mail_data TEXT NOT NULL
);
