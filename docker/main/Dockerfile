# メインのコンテナ
# ビルドはリポジトリトップで行う

# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.10

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    sudo \ 
    locales \
    sqlite3 \
    postfix \
    postfix-sqlite \
    && rm -rf /var/lib/apt/lists/*

# ロケールを設定
RUN locale-gen ja_JP.UTF-8

# 実行ユーザーを作成
RUN groupadd -g 1000 yt_server && \
    useradd -g 1000 -u 1000 -m yt_server

# 作業ディレクトリを設定
WORKDIR /workspace/src

RUN mkdir -p -m 777 /workspace/data

#### Python環境構築 ####

# さしあたってsetuptoolsをインストール
RUN pip install --upgrade pip && \
    pip install setuptools

# Pythonソースコピー
RUN mkdir -p /workspace/src/yt_smtp_catcher && \
    mkdir -p /workspace/src/database
COPY src/yt_smtp_catcher /workspace/src/yt_smtp_catcher
COPY src/database /workspace/src/database
COPY src/setup.py /workspace/src/setup.py
COPY src/setup.cfg /workspace/src/setup.cfg

# pipインストール
RUN pip install -e /workspace/src

# U-DAMはいまのところPyPIにはないので、GitHubから直接インストール
RUN pip install git+https://github.com/shinokiwa/u-dam.git

#### 環境変数の設定 ####
ENV PYTHONPATH=/workspace \
    YT_TSSERVER_DB_PATH=/workspace/data/mail.sqlite3 \
    YT_TSSERVER_SQLITE_PATH=/workspace/sqlite 

#### SQLite3環境構築 ####

# データディレクトリの設定
RUN chmod -R 777 /workspace/data

#### Postfix環境構築 ####

COPY docker/main/etc/postfix/* /etc/postfix/
RUN postmap /etc/postfix/transport

#### エントリーポイントの設定 ####

# 実行スクリプトのコピー
COPY docker/main/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# ポートを開放
EXPOSE 25
EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]