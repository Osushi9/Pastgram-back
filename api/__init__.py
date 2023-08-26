from flask import Flask, make_response, jsonify
from flask_login import LoginManager
from api.models.user import User
from api.views.login import login
from flask_cors import CORS
from api.database import db


app = Flask(__name__)
app.secret_key = "secret_key"

# CORS対応
CORS(app)

# DB設定を読み込む
app.config.from_object("config.Config")
db.init_app(app)

app.register_blueprint(login, url_prefix="/login")

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    """LoginManagerをDBに対して動作させるためのメソッド"""
    return User.query.get(user_id)
