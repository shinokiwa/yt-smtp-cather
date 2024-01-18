#/bin/sh

echo "Starting servers..."

# Postfixが既に起動している場合は停止する
if [ -e /var/spool/postfix/pid/master.pid ]; then
    /usr/sbin/postfix stop
fi

/usr/sbin/postfix start-fg &


# 管理ツールが起動済みの場合は停止する
if [ $(ps -ef | grep -v grep | grep -c "gunicorn") -ne 0 ]; then
    kill -9 `ps -ef | grep -v grep | grep "gunicorn" | awk '{ print $2 }'`
fi

gunicorn -b 0.0.0.0 'yt_testing_smtpserver:create_app()' &