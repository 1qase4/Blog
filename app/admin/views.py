from flask import render_template, redirect, request, url_for, flash, jsonify, make_response
from flask_login import login_user, login_required, logout_user
import json
from functools import partial
from app.models import Article, BlogClassify
from app import db

from . import admin


@admin.route('/edit.html')
def index():
    return render_template('edit.html')
    # return classify('9D4ABD5A8B12')
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


@admin.route('/uploadText', methods=['POST'])
def uploadText():
    name = request.form.get("name", "")
    classification = request.form.get('classification', "")
    content = request.form.get('content', "")
    print(name)
    print(classification)
    print(content)
    article = Article(title=name, classfication=classification, abstract="", content=content)
    db.session.add(article)
    db.session.commit
    return "upload success"
