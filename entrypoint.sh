#!/bin/sh

# Postfixの起動
/usr/sbin/postfix start-fg &

if [ "$DEBUG" = "1" ]; then
    # デバッグモードの場合はFlaskの開発サーバーを起動する
    /usr/local/bin/python3 -m yt_smtp_catcher
else
    # 本番モードの場合はGunicornを起動する
    gunicorn -b 0.0.0.0 'yt_smtp_catcher:create_app()'
fi