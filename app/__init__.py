# -*- coding:utf-8 -*-
# author: zchong

from flask import Flask
from config import Config
#from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)
    #CSRFProtect(app)

    # 初始化db
    db.init_app(app)

    # init public param
    app.config['UPLOAD_FOLDER'] = getUploadPath()

    from .admin import admin
    app.register_blueprint(admin, url_prefix='/admin')

    from .auth import auth
    app.register_blueprint(auth,url_prefix='/auth')

    from .main import main
    app.register_blueprint(main, url_prefix='')

    return app

def getUploadPath():
    import os
    runPath = os.path.split(os.path.realpath(__file__))[0]
    upload = os.path.join(runPath, "static", "upload")
    return upload

