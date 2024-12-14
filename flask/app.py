import os

# Flaskアプリケーションのインスタンス
from flask import Flask
app = Flask(__name__)

# デバッグモードの設定
app.config['DEBUG'] = os.getenv('DEBUG', 'false').lower() == 'true'

# 他の設定も環境変数から取得（オプション）
app.config['ENV'] = os.getenv('FLASK_ENV', 'production')

@app.route('/')
def home():
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=app.config['DEBUG'])