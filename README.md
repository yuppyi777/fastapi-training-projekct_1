# FastAPI Demo Application

実務レベルのFastAPIプロジェクトのデモアプリケーションです。Docker、PostgreSQL、pytest、リンターなど、実際の開発現場で使用される技術スタックを含んでいます。

## 機能

- ユーザー認証（JWT）
- タスク管理CRUD API
- PostgreSQLデータベース
- Docker環境
- 自動テスト（pytest）
- コードリンティング（black, flake8, mypy）

## 技術スタック

- **Framework**: FastAPI 0.109.0
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0 (async)
- **Authentication**: JWT (python-jose)
- **Testing**: pytest, pytest-asyncio
- **Linting**: black, flake8, mypy, isort
- **Container**: Docker, Docker Compose

## プロジェクト構造

```
.
├── app/
│   ├── api/              # APIエンドポイント
│   │   ├── auth.py       # 認証関連
│   │   ├── users.py      # ユーザー関連
│   │   └── tasks.py      # タスク関連
│   ├── core/             # コア機能
│   │   ├── config.py     # 設定
│   │   ├── database.py   # DB接続
│   │   └── security.py   # セキュリティ
│   ├── models/           # データベースモデル
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/          # Pydanticスキーマ
│   │   ├── user.py
│   │   └── task.py
│   ├── services/         # ビジネスロジック
│   │   ├── user_service.py
│   │   └── task_service.py
│   └── main.py           # アプリケーションエントリーポイント
├── tests/                # テストコード
├── migrations/           # DBマイグレーション
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── pyproject.toml
└── Makefile
```

## セットアップ

このプロジェクトは2つの方法で実行できます：
1. **Docker** (推奨) - すべての環境で同じように動作
2. **venv** (ローカル環境) - Windows/Mac/Linux対応

---

## 方法1: Docker環境でのセットアップ (推奨)

### 前提条件

- Docker
- Docker Compose

### インストール

1. リポジトリのクローン

```bash
git clone <repository-url>
cd fastapi-training-project_1
```

2. 環境変数の設定

```bash
cp .env.example .env
# 必要に応じて.envを編集してください
```

3. Docker コンテナの起動

```bash
make install
# または
make build
make up
```

4. アプリケーションの確認

- API: http://localhost:8000
- API ドキュメント: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 方法2: venv環境でのセットアップ (ローカル実行)

### 前提条件

- Python 3.11以上
- PostgreSQL 15以上 (またはDocker)

### セットアップ手順

#### Linux/Mac の場合

1. セットアップスクリプトを実行

```bash
chmod +x setup.sh
./setup.sh
```

2. PostgreSQLの起動（Dockerを使う場合）

```bash
# データベースのみDockerで起動
docker-compose up -d db test_db
```

または、ローカルのPostgreSQLを使う場合は、以下のデータベースを作成：
- `app_db` (開発用)
- `test_db` (テスト用)

3. 環境変数の設定

```bash
cp .env.local .env
# 必要に応じて.envを編集してください
```

4. アプリケーションの起動

```bash
./run_local.sh
```

#### Windows の場合

1. セットアップスクリプトを実行

```cmd
setup.bat
```

2. PostgreSQLの起動（Dockerを使う場合）

```cmd
REM データベースのみDockerで起動
docker-compose up -d db test_db
```

または、ローカルのPostgreSQLを使う場合は、以下のデータベースを作成：
- `app_db` (開発用)
- `test_db` (テスト用)

3. 環境変数の設定

```cmd
copy .env.local .env
REM 必要に応じて.envを編集してください
```

4. アプリケーションの起動

```cmd
run_local.bat
```

### venv環境でのテスト実行

#### Linux/Mac

```bash
./run_tests.sh
# または
source venv/bin/activate
pytest
```

#### Windows

```cmd
run_tests.bat
REM または
venv\Scripts\activate
pytest
```

### venv環境でのリント/フォーマット

```bash
# Linux/Mac
source venv/bin/activate
black app tests
flake8 app tests
mypy app

# Windows
venv\Scripts\activate
black app tests
flake8 app tests
mypy app
```

---

## 使い方

### Makeコマンド

```bash
make help          # ヘルプを表示
make build         # Dockerイメージをビルド
make up            # コンテナを起動
make down          # コンテナを停止
make restart       # コンテナを再起動
make logs          # ログを表示
make shell         # アプリケーションシェルにアクセス
make db-shell      # データベースシェルにアクセス
make test          # テストを実行
make test-cov      # カバレッジ付きテストを実行
make lint          # リンターを実行
make format        # コードをフォーマット
make clean         # クリーンアップ
```

### API エンドポイント

#### 認証

- `POST /api/auth/register` - ユーザー登録
- `POST /api/auth/login` - ログイン

#### ユーザー

- `GET /api/users/me` - 現在のユーザー情報取得
- `PUT /api/users/me` - 現在のユーザー情報更新
- `GET /api/users/{user_id}` - ユーザー情報取得

#### タスク

- `GET /api/tasks/` - タスク一覧取得
- `POST /api/tasks/` - タスク作成
- `GET /api/tasks/{task_id}` - タスク詳細取得
- `PUT /api/tasks/{task_id}` - タスク更新
- `DELETE /api/tasks/{task_id}` - タスク削除

### テストの実行

```bash
# 全テストを実行
make test

# カバレッジ付きで実行
make test-cov

# 特定のテストファイルを実行
docker-compose exec app pytest tests/test_auth.py
```

### コードフォーマット

```bash
# コードをフォーマット
make format

# フォーマットチェックのみ
make format-check

# リンターを実行
make lint
```

## 受講生向けの課題

このプロジェクトには、学習目的でいくつかのバグや未実装の機能が含まれています。

### 📚 課題に取り組む前に

**必ず `課題の進め方.md` を読んでください！**

このファイルには以下が含まれています：
- 課題の詳細な説明
- 実装のヒント
- テストの書き方
- 確認方法
- よくある質問

### 課題一覧

全部で6つの課題があります。**必ず1つずつ順番に**取り組んでください。

#### バグ修正課題（2件）
1. タスクモデルのリレーションシップ修正
2. 完了タスク数の集計バグ修正

#### 機能追加課題（3件）
3. タスク統計エンドポイント実装
4. 優先度フィルター実装
5. タスク検索機能実装

#### メイン課題（1件）⭐
6. カテゴリ管理API実装（サービス層、エンドポイント、テスト）

### 課題の進め方

1. 環境構築（Docker推奨）
2. `課題の進め方.md` を読む
3. 課題1から順番に実装
4. 各課題ごとにテストを書く
5. テストがパスすることを確認
6. コミット・プッシュして講師に報告
7. **講師の確認を待つ** ← 重要！
8. 次の課題に進む

### 完了基準

各課題ごとに：
```bash
# すべてのテストがパス
pytest

# コミット・プッシュ
git add .
git commit -m "Complete task X: ..."
git push

# 講師に報告
```

詳細は **`課題の進め方.md`** を参照してください

---

## トラブルシューティング

### Docker環境の問題

#### アプリケーションが起動しない

```bash
# Dockerが起動しているか確認
docker ps

# コンテナの状態を確認
docker-compose ps

# ログを確認
docker-compose logs app
docker-compose logs db
```

#### ポートが既に使用されている

```bash
# Mac/Linux: ポート使用状況を確認
lsof -i :8000
lsof -i :5432

# Windows: ポート使用状況を確認
netstat -ano | findstr :8000
netstat -ano | findstr :5432

# 解決方法: docker-compose.ymlのポート番号を変更
# ports:
#   - "8001:8000"  # 8000 → 8001に変更
```

#### データベース接続エラー

```bash
# DBコンテナが起動しているか確認
docker-compose ps db

# DBの起動を待ってから再起動
docker-compose down
docker-compose up -d db
sleep 5
docker-compose up -d app
```

### venv環境の問題

#### Python が見つからない

```bash
# Mac
brew install python@3.11

# Ubuntu/Debian
sudo apt-get install python3.11

# Windows
# https://www.python.org/ からダウンロードしてインストール
```

#### 依存関係のインストールエラー

```bash
# Mac: PostgreSQLクライアントライブラリが必要
brew install postgresql

# Ubuntu/Debian
sudo apt-get install libpq-dev python3-dev

# Windows: Microsoft C++ Build Toolsが必要な場合あり
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

#### データベース接続エラー

```bash
# .envファイルの DATABASE_URL を確認
cat .env

# PostgreSQLが起動しているか確認（Dockerの場合）
docker-compose ps db

# ローカルPostgreSQLの場合
# Mac
brew services list | grep postgresql

# Linux
sudo systemctl status postgresql
```

### テスト関連の問題

#### テストが失敗する

```bash
# テスト用DBが起動しているか確認
docker-compose ps test_db

# テスト用DBを再起動
docker-compose restart test_db

# .env の TEST_DATABASE_URL を確認
grep TEST_DATABASE_URL .env
```

#### テストが遅い

```bash
# テスト用DBのみ起動してテスト実行
docker-compose up -d test_db
./run_tests.sh

# 特定のテストのみ実行
pytest tests/test_auth.py -v
```

### よくある質問

#### Q: Windows で `./setup.sh` が実行できない
A: Windows では `setup.bat` を使用してください。

#### Q: `make` コマンドが使えない
A: Makefileは主にDockerコマンドのショートカットです。`docker-compose`コマンドを直接使用できます。

```bash
# make build の代わり
docker-compose build

# make up の代わり
docker-compose up -d

# make test の代わり
docker-compose exec app pytest
```

#### Q: API ドキュメントが開けない
A: ブラウザで http://localhost:8000/docs にアクセスしてください。アプリケーションが起動していることを `docker-compose ps` で確認してください。

#### Q: 課題の答えはありますか？
A: 課題の答えは用意していません。参考ファイル（`app/services/task_service.py`や`app/api/tasks.py`）を見ながら、自分で実装してください。

---

## ライセンス

MIT License

## 参考リンク

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [pytest Documentation](https://docs.pytest.org/)
