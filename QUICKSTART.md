# クイックスタートガイド

すぐに始めたい方向けの最速スタートガイドです。

詳細なドキュメントは [README.md](README.md) を参照してください。

---

## 🚀 5分で始める（推奨）

### Docker版

```bash
# 1. プロジェクトに移動
cd fastapi-training-project_1

# 2. 起動（初回は5-10分かかります）
docker-compose up -d

# 3. ブラウザで開く
# http://localhost:8000/docs
```

**完了！** APIドキュメントが開きます。

---

## 💻 venv版

### Mac/Linux

```bash
# 1. セットアップ（初回のみ）
./setup.sh

# 2. DBを起動
docker-compose up -d db test_db

# 3. アプリ起動
./run_local.sh

# 4. ブラウザで開く
# http://localhost:8000/docs
```

### Windows

```cmd
REM 1. セットアップ（初回のみ）
setup.bat

REM 2. DBを起動
docker-compose up -d db test_db

REM 3. アプリ起動
run_local.bat

REM 4. ブラウザで開く
REM http://localhost:8000/docs
```

---

## 🧪 テスト実行

```bash
# Docker版
docker-compose exec app pytest

# venv版（Mac/Linux）
./run_tests.sh

# venv版（Windows）
run_tests.bat
```

---

## 🎯 次のステップ

1. **APIを試す**: http://localhost:8000/docs でユーザー登録 → ログイン → タスク作成

2. **課題に挑戦**: [README.md](README.md) の「受講生向けの課題」セクションを確認
   - バグ修正課題（簡単）
   - 機能追加課題（中級）
   - **⭐ カテゴリAPI実装課題（メイン課題）**

3. **詳細を確認**: [README.md](README.md) で詳しい説明を読む

---

## ❓ 困ったら

### Docker版で起動しない
```bash
# Dockerが起動しているか確認
docker ps

# ログを確認
docker-compose logs
```

### venv版でエラー
```bash
# Python バージョン確認（3.11以上が必要）
python3 --version

# 環境変数を確認
cat .env
```

### それでも解決しない場合
[README.md](README.md) の「トラブルシューティング」セクションを参照してください。

---

**📖 詳しい説明が必要な場合は [README.md](README.md) をご覧ください**
