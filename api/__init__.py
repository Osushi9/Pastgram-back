from flask import Flask, make_response, jsonify
from flask_login import LoginManager
from api.views.user import user_router
from api.views.page import page_router
from api.views.auth import auth
from api.views.home import home
from api.views.storage import storage_router
from flask_cors import CORS
from api.database import db


app = Flask(__name__)
app.secret_key = "secret_key"

# CORS対応
CORS(app)

# DB設定を読み込む
app.config.from_object("config.Config")
db.init_app(app)


app.register_blueprint(user_router, url_prefix="/api")
app.register_blueprint(page_router, url_prefix="/page")
app.register_blueprint(storage_router, url_prefix="/storage")

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from api.models.users import Users
    """LoginManagerをDBに対して動作させるためのメソッド"""
    return Users.query.get(user_id)
