# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.10 as yt_testing_smtpserver

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    locales \
    sqlite3 \
    postfix \
    && rm -rf /var/lib/apt/lists/*

# ロケールを設定
RUN locale-gen ja_JP.UTF-8

# 実行ユーザーを作成
RUN groupadd -g 1000 yt_server && \
    useradd -g 1000 -u 1000 -m yt_server

# 作業ディレクトリを設定
WORKDIR /workspace

# 使用するディレクトリを一括作成
RUN mkdir -p /entrypoint && \
    mkdir -p /workspace/sqlite && \
    mkdir -p /workspace/data && \
    mkdir -p /workspace/yt_testing_smtpserver

#### SQLite3環境構築 ####

# DBの初期化
COPY sqlite/create_database.sql /workspace/sqlite/create_database.sql
RUN sqlite3 /workspace/data/mail.sqlite3 < /workspace/sqlite/create_database.sql
RUN chmod -R 777 /workspace/data

#### Python環境構築 ####

# さしあたってsetuptoolsをインストール
RUN pip install --upgrade pip && \
    pip install setuptools

# Pythonソースコピー
RUN mkdir -p /workspace/yt_testing_smtpserver
COPY yt_testing_smtpserver /workspace/yt_testing_smtpserver
COPY setup.py /workspace/setup.py
COPY setup.cfg /workspace/setup.cfg

# PYTHONPATHを設定
ENV PYTHONPATH=/workspace

# pipインストール
RUN pip install -e /workspace

# Postfixの設定
COPY postfix/* /etc/postfix/
RUN postmap /etc/postfix/transport

# 実行スクリプトのコピー
COPY entrypoint/* /entrypoint/
RUN chmod +x /entrypoint/*

# ポートを開放
EXPOSE 25
EXPOSE 8000

ENTRYPOINT ["/entrypoint/entrypoint.sh"]

