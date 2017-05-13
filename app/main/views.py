# -*- coding:utf-8 -*-
# author: zchong

from flask import render_template, redirect, request, url_for, flash, jsonify, make_response
from flask_login import login_user, login_required, logout_user
import json
from functools import partial
from app.models import Blog, BlogClassify

from . import main


@main.route('/index')
def index():
    return classify('9D4ABD5A8B12')
    # o = User.query.all()
    # print(o.__dict__)
    # author='zchong'
    # json_str = jsonify(o)
    # return render_template("index.html",author=author)
    # return make_response(jsonify(o.__dict__))
    # print(o.alias)
    # json_dumps = partial(json.dumps, ensure_ascii=False, sort_keys=True)
    # return jsonify("张冲是我")
    # classifys = Classify.getClassifys()



@main.route('/classify/<string:id>/')
def classify(id):
    blogs = Blog.query.with_entities(Blog.id, Blog.title, Blog.summary).join(BlogClassify).filter(
        BlogClassify.classify_id == '9D4ABD5A8B12')
    print(blogs)
    return render_template('index.html', blogs=blogs)

@main.route('/content/<string:id>/')
def content(id):
    print(id)
    blog = Blog.query.filter(id==id).first()
    return render_template('content.html',blog=blog)
