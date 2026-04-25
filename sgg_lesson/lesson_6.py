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