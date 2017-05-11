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

    @property
    def json(self):
        return to_json(self, self.__class__)

# 博客信息
class Blog(db.Model):
    __tablename__ = 'blog'

    id = db.Column(db.CHAR(12),primary_key=True)
    title = db.Column(db.String(512))
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

# 分类
class Classify(db.Model):
    __tablename__ = 'classify'
    id = db.Column(db.CHAR(12),primary_key=True)
    name = db.Column(db.String(128))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

# 博客-分类信息
class BlogClassify(db.Model):
    __tablename__ = 'blog_classify'
    id = db.Column(db.CHAR(12), primary_key=True)
    blog_id = db.Column(db.CHAR(12))
    classify = db.Column(db.CHAR(12))
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
    return json.dumps(d,ensure_ascii=False)
