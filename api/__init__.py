from flask import Flask
from flask_login import LoginManager
from api.views.auth import auth
from api.views.home import home
from flask_cors import CORS
from api.database import db


app = Flask(__name__)
app.secret_key = "secret_key"

# CORS対応
CORS(app)

# DB設定を読み込む
app.config.from_object("config.Config")
db.init_app(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(home, url_prefix="/home")

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from api.models.users import Users
    """LoginManagerをDBに対して動作させるためのメソッド"""
    return Users.query.get(user_id)
