# -*- coding:utf-8 -*-
# author: nulige

class Config():
    DEBUG = True

    SECRET_KEY = 'secret key to protect from csrf'

    # 数据库配置  '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@127.0.0.1:3306/blog?charset=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    # 打印sql语句   参见 http://www.pythondoc.com/flask-sqlalchemy/config.html
    SQLALCHEMY_ECHO=True

    JSON_AS_ASCII=False
    @staticmethod
    def init_app(app):
        pass
