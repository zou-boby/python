""""
字典dict

"""

tech = {
    'name': 'xiao',
    'age': 21,
    'gender': 'male',
    'score': {
        '语文': 90,
        'math': 99
    },
}
print(type(tech))
tech['position'] = 'monitor'
print(tech)
print(tech['name'])
tech['name'] = 'zjr'
print(tech)

# del tech['name']
# print(tech)

print('name' in tech)

# 字典的遍历
for i in tech:
    print(i, tech[i])

#dict_items([('name', 'zjr'), ('age', 21), ('gender', 'male'), ('score', {'语文': 90, 'math': 99}), ('position', 'monitor')]) 是元组
print(tech.items())
for k, v in tech.items(): # 用k v 解构元组
    print(k, v)

for k in tech.keys():
    print(k, tech[k])
for v in tech.values():
    print(v)

print("*" * 20)
# 字典的常用方法
res = tech.pop('name')
print(res)

res = tech.copy()
print(res)
tech['name'] = 'zjr'
res = tech.get('name')
print(res)
res = tech.popitem()
print(tech, res)
tech.update({'name': 'xiao', 'age': 44, 'gender': 'male'}) # 有就进行修改，没有就添加
print(tech)


# 定义（2）
d2 = dict([('name', 'saa'), ('age', 44), ('gender', 'male')])
print(d2)

d2.update({'name': 'zjr', 'age': 24, 'gender': 'female', 'score': {'语文': 99, 'math': 99}})
print(d2)


# 嵌套查询
stu = {
   20260427: {
       'name': 'xiao',
       'age': 44,
       'hobby': ['ball', 'swing']
   }
}
print(stu[20260427]['hobby'])

keys = stu[20260427].keys()
print(type(res), res)
vals = stu[20260427].values()
print(type(vals), vals)

items = stu[20260427].items()
print(type(items), items)

# 字典的遍历
for key in stu[20260427].keys():
    print(key, stu[20260427][key])

print('---'*5)

for k, v in stu[20260427].items():
    print(k, v)

