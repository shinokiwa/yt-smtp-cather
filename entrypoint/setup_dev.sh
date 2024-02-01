# !/bin/sh

# 開発環境用の設定
# GitとDockerをインストールする

apt-get update
apt-get install -y git

apt-get purge lxc-docker*
apt-get purge docker.io*

# Dockerの公式GPGキーを追加
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Dockerのリポジトリをリストに追加
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

# パッケージリストを更新
apt-get update

# Dockerをインストール
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

cd /workspace/
pip install .[dev]