# -*- coding:utf-8 -*- 
# author: zchong
# -*- coding: UTF-8 -*-
import json
import datetime
from app.utils import CJsonEncoder
# 自定义类
class MyClass:
    # 初始化
    def __init__(self):
        self.a = 2
        self.b = 'bb'
        self.t = datetime.datetime.now()

# 创建MyClass对象
myClass = MyClass()
# 添加数据c
myClass.c = 123
myClass.a = 3
# 对象转化为字典
myClassDict = myClass.__dict__
# 打印字典
print(myClassDict)
# 字典转化为json
myClassJson = json.dumps(myClassDict,cls=CJsonEncoder)
# 打印json数据
print(myClassJson)

##########################
# json转化为字典
myClassReBuild = json.loads(myClassJson)
# 打印重建的字典
print(myClassReBuild)
# 新建一个新的MyClass对象
myClass2 = MyClass()
# 将字典转化为对象
myClass2.__dict__ = myClassReBuild;
# 打印重建的对象
print(myClass2.a)
