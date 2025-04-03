from flask import Flask
from routes import register_blueprints

app = Flask(__name__)  # Flaskアプリのインスタンスを作成

register_blueprints(app)  # BlueprintのルートをFlaskアプリに登録

if __name__ == '__main__':
    app.run(debug=True)  # デバッグモードでFlaskアプリを実行