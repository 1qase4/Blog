# -*- coding:utf-8 -*- 
# author: zchong
import json
import uuid

from datetime import datetime, date

def getUUID():
    str = uuid.uuid1().__str__()
    list = str.split('-')
    return (list[0] + list[3]).upper()

if __name__ == '__main__':
    print(getUUID())