# DevContainer用のDockerfile

# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.10 as yt_testing_smtpserver

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    git \
    locales \
    postfix \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# ロケールを設定
RUN locale-gen ja_JP.UTF-8

# Postfixの設定
COPY postfix/* /etc/postfix/
RUN postmap /etc/postfix/transport

# Postfixがスクリプトを実行するためのユーザーを作成
RUN groupadd -g 1000 yt_server && \
    useradd -g 1000 -u 1000 -m yt_server

# 作業ディレクトリを設定
WORKDIR /workspace

# PYTHONPATHを設定
ENV PYTHONPATH=/workspace

# 本来ならpipインストールとかあるけど、今のところ何もない。

# ポート25を開放
EXPOSE 25

# 実行スクリプトのコピー
COPY docker/start_servers.sh /start_servers.sh
RUN ["chmod", "+x", "/start_servers.sh"]

COPY docker/entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]

# DBの初期化
RUN mkdir -p /workspace/data
COPY sqlite/create_database.sql /workspace/sqlite/create_database.sql
RUN sqlite3 /workspace/data/mail.sqlite3 < /workspace/sqlite/create_database.sql
RUN chown -R yt_server:yt_server /workspace/data && \
    chmod -R 777 /workspace/data

ENTRYPOINT ["/entrypoint.sh"]
