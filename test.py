import uuid

str = uuid.uuid1().__str__()
print(str)
list = str.split('-')
print(list[0]+list[3])

