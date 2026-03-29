# 列表 --- 数组

list=["张三", "里斯", "王五"]
print(list)

list.append("abc")
# print(list.pop(2))
print(list.pop(1))
print(list)
list[0]="张三李四"
print(list)

ls=[
    ['aa','bb','cc'],
    ['dd','ee','ff']
]
print(ls[0][0])


d1={"name":"张三", "age":18}
print(d1)
d4=dict([('name', 'zhangs'),('age', 18)])
print(d4)
d4.update({'name':'sss','age':22, 'score':[88,90,22]})
print(d4)
d4['name']='fw'
print(d4)
print(len(d4))