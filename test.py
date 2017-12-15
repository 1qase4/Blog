import uuid

# str = uuid.uuid1().__str__()
# print(str.upper())
# list = str.split('-')
# print(list[0]+list[3])

import time
import datetime

t = time.time()
import json
data = {
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
}

json_str = json.dumps(data)
print(json_str)


