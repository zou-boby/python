# 列表 --- 数组

list1=["张三", "里斯", "王五"]
print(list1)

list1.append("abc")
# print(list1.pop(2))
print(list1.pop(1))
print(list1)
list1[0]="张三李四"
print(list1)

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


#score=int( input("输入分数：\n") )
score=80
if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("E")



names=['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
print('Bob' in names)
sum=0
for num in range(10):
    sum+=num
print(sum)

print(list(range(6)))

sum=0;i=1
while(i<100):
    sum+=i
    i+=1
print(sum)