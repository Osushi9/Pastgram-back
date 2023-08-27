from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# アプリでDB操作を行えるように初期設定する
def init_db(app):
    db.init_app(app)
