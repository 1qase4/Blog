# -*- coding:utf-8 -*-
# author: zchong

from flask import render_template, redirect, request, url_for, flash, jsonify, make_response
from flask_login import login_user, login_required, logout_user
import json
from functools import partial
from app.models import Article, BlogClassify
from manage import app
import os

from . import main

@main.route('/')
@main.route('/index.html')
def index():
    return render_template('index.html')
    #return classify('9D4ABD5A8B12')
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

import time
import json
@main.route('/upload',methods=['GET', 'POST'])
def upload():
    path = app.config['UPLOAD_FOLDER']
    file = request.files['upfile']
    originalName = file.filename
    size = file.__sizeof__()
    type = os.path.splitext(originalName)[1]
    fileName = "%d%s" % (time.time(), type)
    file.save(os.path.join(path,fileName))
    print(file.name)
    res = {"name":fileName,
           "originalName":originalName,
           "size":size,
           "state": "SUCCESS",
           "url": fileName
           }

    return json.dumps(res)


@main.route('/blog/<int:id>/')
def showBlog(id):
    print(id + 1)
    article = Article.query.filter_by(id=id).first()

    return render_template("blog.html", article=article)


@main.route('/about.html')
def about():
    return render_template("about.html")

@main.route('/messageBoard.html')
def messageBoard():
    return render_template("messageBoard.html")

@main.route('/classify/<string:id>/')
def classify(id):

    blogs = Article.query.with_entities(Article.id, Article.title, Article.summary).join(BlogClassify).filter(
        BlogClassify.classify_id == id)
    print(blogs)
    return render_template('index.html', blogs=blogs)

@main.route('/content/<string:id>/')
def content(id):
    print(id)
    blog = Article.query.filter(id == id).first()
    return render_template('content.html',blog=blog)


@main.route('/test')
def test():
    return render_template("test.html")



@main.route('/test1',methods=['GET', 'POST'])
def test1():
    if request.method == 'POST':
        file = request.files['file']

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''