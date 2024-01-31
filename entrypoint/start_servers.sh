#!/bin/sh

echo "Starting servers..."

# Postfixが既に起動している場合は停止する
if [ -e /var/spool/postfix/pid/master.pid ]; then
    /usr/sbin/postfix stop
fi

/usr/sbin/postfix start-fg &


if [ "$DEBUG" = "1" ]; then
    # デバッグモードの場合はFlaskの開発サーバーを起動する
    if [ $(ps -ef | grep -v grep | grep -c "/usr/local/bin/python3") -ne 0 ]; then
        kill -9 `ps -ef | grep -v grep | grep "/usr/local/bin/python3" | awk '{ print $2 }'`
    fi
    /usr/local/bin/python3 -m yt_testing_smtpserver &

else
    # 本番モードの場合はGunicornを起動する
    if [ $(ps -ef | grep -v grep | grep -c "gunicorn") -ne 0 ]; then
        kill -9 `ps -ef | grep -v grep | grep "gunicorn" | awk '{ print $2 }'`
    fi
    gunicorn -b 0.0.0.0 'yt_testing_smtpserver:create_app()' &
fi