# 1. ビルド環境 (Node.jsを使用)
FROM node:23.0.0-alpine AS builder

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール (package.json, package-lock.jsonを使用)
COPY app/package*.json ./
RUN npm install

# Next.jsのコードをコピー
COPY app/ .

# Next.jsをビルド
RUN npm run build

# 2. 実行環境 (軽量化のために再度Node.jsの小さなイメージを使用)
FROM node:23.0.0-alpine AS runner

# 作業ディレクトリの設定
WORKDIR /app

# ビルド結果をコピー
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/node_modules ./node_modules

# Next.jsが使用するポートを開放
EXPOSE 3000

# SSRサーバーを起動
CMD ["npm", "run", "start"]
