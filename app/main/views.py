# -*- coding:utf-8 -*-
# author: zchong

from flask import render_template, redirect, request, url_for, flash, jsonify, make_response
from flask_login import login_user, login_required, logout_user
import json
from functools import partial

from . import main

from ..models import User,Classify

@main.route('/test')
def test():
    o = User.query.all()
    # print(o.__dict__)
    # author='zchong'
    # json_str = jsonify(o)
    #return render_template("index.html",author=author)
    #return make_response(jsonify(o.__dict__))
    #print(o.alias)
    json_dumps = partial(json.dumps, ensure_ascii=False, sort_keys=True)
    return jsonify("张冲是我")

@main.route('/classify/<string:id>/')
def index(id):
    # 获取分类信息
    # classifys =Classify.query.filter_by(id=id).first()
    # print(classifys.name)
    classifys = Classify.query.filter_by(id=id).all()

    return render_template('index.html', classifys=classifys)
