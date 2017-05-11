# -*- coding:utf-8 -*-
# author: zchong

from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    CSRFProtect(app)

    # 初始化db
    db.init_app(app)

    from .admin import admin
    app.register_blueprint(admin, url_prefix='/auth')

    from .auth import auth
    app.register_blueprint(auth,url_prefix='/auth')

    from .main import main
    app.register_blueprint(main, url_prefix='/main')

    return app

