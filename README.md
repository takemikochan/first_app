# Flask API with Blueprint

このプロジェクトは、Flaskを使ってシンプルなAPIを構築するサンプルアプリです。  
Blueprintを使用して、アプリの構成に拡張性を持たせた設計をしています。

## 概要

- `/api/greet?name=YOUR_NAME` にアクセスすると、指定した名前を使って挨拶を返すAPIを実装
- Flask + Blueprint による拡張性のある構成
- 本番環境では Gunicorn + Nginx によるデプロイを想定

## セットアップ手順

### 必要な環境

- Python 3.8 以上
- pip（Pythonパッケージマネージャ）

### 仮想環境の作成

```bash
python -m venv venv
```

### 仮想環境の有効化

- Windows:
  ```bash
  .\venv\Scripts\activate
  ```

- Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### パッケージのインストール

```bash
pip install -r requirements.txt
```

## 起動方法

### 開発用サーバー

```bash
python app.py
```

### WSGIサーバー（Linux環境）

```bash
gunicorn --bind 127.0.0.1:8000 app:app
```

> ⚠️ Windows環境では gunicorn は利用できません。VPS上で使用します。

## エンドポイント

### GET `/api/greet`

- クエリパラメータ: `name`（例: `?name=みこと`）
- レスポンス例：

```json
{
  "message": "こんにちは, みこと!"
}
```

## ディレクトリ構成（抜粋）

```
first_app/
├── app.py                  # アプリのエントリポイント
├── routes/                 # ルーティングを定義したBlueprintモジュール
│   ├── __init__.py         # Blueprint登録と構成用
│   └── greet.py            # `/api/greet` のルーティング処理
├── requirements.txt
├── README.md
└── ...
```

## 開発者

- **名前**: みことちゃん
- **GitHub**: [https://github.com/takemikochan](https://github.com/takemikochan)

## ライセンス

このプロジェクトは [MIT License](LICENSE) のもとで公開されています。