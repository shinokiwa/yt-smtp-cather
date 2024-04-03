# 開発用コンテナ
# 基本イメージとしてPythonの公式イメージを使用
FROM python:3.10

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y \
    locales \
    sqlite3

# ロケールを設定
RUN locale-gen ja_JP.UTF-8

# DockerオフィシャルのGPGキーを追加
RUN install -m 0755 -d /etc/apt/keyrings && \
    curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
    chmod a+r /etc/apt/keyrings/docker.asc

# Dockerのリポジトリを追加
RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

# aptのキー削除
RUN rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /workspace

# 使用するディレクトリを一括作成
RUN mkdir -p -m 777 /workspace/data

#### Python環境構築 ####

# さしあたってsetuptoolsをインストール
RUN pip install --upgrade pip && \
    pip install setuptools

# Pythonソースコピー
RUN mkdir -p /workspace/yt_smtp_catcher && \
    mkdir -p /workspace/database
COPY yt_smtp_catcher /workspace/yt_smtp_catcher
COPY database /workspace/database
COPY setup.py /workspace/setup.py
COPY setup.cfg /workspace/setup.cfg

# pipインストール
RUN pip install -e /workspace[dev]

# U-DAMはいまのところPyPIにはないので、GitHubから直接インストール
RUN pip install git+https://github.com/shinokiwa/u-dam.git

#### 環境変数の設定 ####
ENV PYTHONPATH=/workspace \
    YT_TSSERVER_DB_PATH=/workspace/data/mail.sqlite3 \
    YT_TSSERVER_SQLITE_PATH=/workspace/sqlite 

CMD ["tail", "-F", "/dev/null"]