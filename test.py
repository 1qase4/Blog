import uuid

str = uuid.uuid1().__str__()
print(str.upper())
list = str.split('-')
print(list[0]+list[3])

