# python:3.13-slimを使用
FROM python:3.13.0-slim

# 作業ディレクトリを作成
WORKDIR /app

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y gcc musl-dev && rm -rf /var/lib/apt/lists/*

# uwsgi.iniをコピー
COPY environments/uwsgi.ini .

# requirements.txtをコピーして必要なパッケージをインストール
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードと設定ファイルをコピー
COPY app/ .

# ユニットテストを実行
RUN python -m unittest discover tests

# uWSGIの起動コマンドを指定
CMD ["uwsgi", "--ini", "uwsgi.ini"]
