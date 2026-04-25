"""
1. 列表 [] / list()
    列表的创建、索引
    列表的遍历
    列表的常用方法
2. 元组 ()
    不能修改
    只有一个元素 (0,)  (1)就不是元组
    元组的遍历
    元组的切片、拼接
    元组的常用方法

"""

a = [1, 2]
b = [3, 4]
print(a + b)
print(a * 4)
print(3 in a)
print(4 in b)

print(type(a))
c = list(range(5))
print(c, type(c))

d = list(range(10))
print(d, type(d))
print(d[9])

print(len(d))
print(max(d))
print(min(d))
# del d # 删除

# 列表的遍历
# for i in d:
#     print(i, end=" ")
for i, j in enumerate(d):  # 枚举 i为下标
    print(i, j, end=" ")
print("\n")
# 列表的常用方法
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)  # 直接把list2作为一个元素 放到末尾
print(list1)
list1.extend(list2)  # 把list2中的元素逐个放进list1中，相当于 list1 + list2
print(list1)

list1.remove(list2)  # remove删除 是 从前往后找第一个删除
print(list1)
list1.insert(1, list2)
print(list1)

rs = list1.pop(1)
print(list1)
print(rs)
list1.reverse()
print(list1)
rs.reverse()
print(rs)

r1 = list1.sort()  # return None
print(list1, r1)

print(sum(list1) / len(list1))

# 元组
tuple1 = tuple()
print(tuple1)
tuple2 = (1,)
print(tuple2)
tuple3 = (0)
print(tuple3)

tuple4 = tuple('hello world')  # str --> tuple
print(tuple4)
tuple5 = tuple([5, 6, 7, 8])  # list ---> tuple
print(tuple5)

list11 = list(tuple5)  # tuple --> list
print(list11)
str1 = str(tuple5)
print(str1)

# 索引
print(tuple5[3])
print(tuple5[::-1])
print(len(tuple5))
print(max(tuple5))
print(min(tuple5))
del tuple5
# print(tuple5)

print("*" * 10)
# 拼接
print(tuple4 + tuple2)
print(tuple2, tuple2 * 2)
print(tuple4, 'h' in tuple4)

list11[1] = 9
print(list11)

# tuple4[4] = 1 # 无法修改
print(tuple4)

tuple4.count('h')
print(tuple4)
a = tuple4.count('h')
print(a)
print(tuple4.index('h'))

# 元组的遍历
for i in tuple4:
    print(i)
for index, value in enumerate(tuple4):
    print(index, value)

# 水仙花数 各位的立方和==本身
for i in range(100, 1000):
    # a = i % 10
    # b = i // 10 % 10
    # c = i // 100

    iStr = str(i)
    a = int(iStr[2])
    b = int(iStr[1])
    c = int(iStr[0])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)
