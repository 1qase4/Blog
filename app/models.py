# -*- coding:utf-8 -*- 
# author: zchong

import json

from datetime import datetime
from sqlalchemy import DateTime


from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    alias = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)
    createdt = db.Column(db.DateTime)
    updatedt = db.Column(db.DateTime)




# 博客信息
class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(128))
    classfication = db.Column(db.String(32))
    abstract = db.Column(db.String(4000))
    content = db.Column(db.Text)
    author = db.Column(db.String(32))
    createdt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedt = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,title,classfication,abstract,content):
        self.title = title
        self.classfication = classfication
        self.abstract = abstract
        self.content = content
        self.author = 'zchong'
        # self.createdt = datetime.utcnow
        # self.updatedt = datetime.utcnow

# 分类
class Classify(db.Model):
    __tablename__ = 'classify'
    id = db.Column(db.CHAR(12), primary_key=True)
    name = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

    # 获取所有的分类
    @staticmethod
    def getClassifys():
        classifys = Classify.query.all()
        return classifys


# 博客-分类信息
class BlogClassify(db.Model):
    __tablename__ = 'blog_classify'

    id = db.Column(db.CHAR(12), primary_key=True)
    blog_id = db.Column(db.CHAR(12), db.ForeignKey('blog.id'))
    classify_id = db.Column(db.CHAR(12), db.ForeignKey('classify.id'))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)


def datetimestr(datetime):
    return datetime.strftime('%Y-%m-%d %H:%M:%S')


def to_json(inst, cls):
    convert = dict()
    convert[datetime] = datetimestr
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if type(v) in convert.keys() and v is not None:
            try:
                d[c.name] = convert[type(v)](v)
            except:
                d[c.name] = "Error: Failed to covert using ", str(convert[c.type])
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d, ensure_ascii=False)
