#/bin/sh

echo "Starting servers..."

# Postfixが既に起動している場合は停止する
if [ -e /var/spool/postfix/pid/master.pid ]; then
    /usr/sbin/postfix stop
fi

/usr/sbin/postfix start-fg &