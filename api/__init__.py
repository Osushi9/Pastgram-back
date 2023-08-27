from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from api.database import db
from api.views.auth import auth
from api.views.home import home
from api.views.api import api
from api.views.page import page
from api.views.storage import storage_router

app = Flask(__name__)
app.secret_key = "secret_key"

# CORS対応
CORS(app)

# DB設定を読み込む
app.config.from_object("config.Config")
db.init_app(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(page, url_prefix="/page")
app.register_blueprint(storage_router, url_prefix="/storage")
app.register_blueprint(api, url_prefix="/api")

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from api.models.users import Users

    """LoginManagerをDBに対して動作させるためのメソッド"""
    return Users.query.get(user_id)
