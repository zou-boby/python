"""
数据处理的常用函数
- map函数
    map(操作函数，可迭代对象）
    功能：对一组数据中的每个元素 统一执行某种操作，并生成一组新数据
    返回值：迭代器对象，需要手动遍历或者类型转换

    注意点⚠️：
    1. 延迟执行： map不会立刻计算，只有在需要计算的时候才会执行
    2. 返回的是迭代器对象，一旦遍历完成，就会被耗尽
    3. map不会改变元素的个数

- filter函数
    filter(过滤函数, 可迭代对象）
    功能：从一组数据中筛选出符合条件的元素并形成一组新的数据
    原理：
        def filter(function, iterable):
        for item in iterable:          # 遍历 person 列表
            if function(item):         # 对每个 item 调用 lambda 函数
                yield item             # 如果返回 True，保留该 item

    ⚠️：filter可能会影响元素的数量
    filter特殊用法：当 filter 的第一个参数是 None 时，它会自动把可迭代对象中的每个元素当作布尔值判断，只保留那些“真值”（truthy）的元素。



- sorted函数
    sorted(可迭代对象，key=xxx，reverse=True)
    功能：对一组数据进行排序，返回一组新数据


- reduce函数
    reduce(合并函数，可迭代对象，初始值)
    功能：将一组数据不断‘合并’，最终归并成一个结果
    需要先引入 from functools import reduce

    initial_missing = object()
"""
from mimetypes import init

nums = [10, 20, 30]
def double(x):
    return x * 2
# 返回值：迭代器对象，需要手动遍历或者类型转换

res = map(double, nums)
print(list(res)) # 延迟执行： map不会立刻计算，只有在需要计算的时候才会执行, 也就是在遍历的时候

# 用匿名函数作为操作函数
res = map(lambda x: x * 2, nums)
print(list(res))


# 字符串转换
names = ('python', 'java', 'ruby')
res = map(lambda x: x.upper(), names)
print(tuple(res))
# 类型转换
str_num = {'1', '2', '3'}
int_num = map(int, str_num)
print(set(int_num)) # {1, 2, 3} 返回的是迭代器对象 一旦遍历完成，就会被耗尽
print(set(int_num)) # set()


# filter函数
nums = [10, 20, 30, 40]
res = filter(lambda n : n < 30, nums)
print(list(res)) # [10, 20]
print(nums) # [10, 20, 30, 40] 不会破坏原数据
print(list(res)) # [] 同样会被耗尽


# filter会遍历person，并将其中的每一项传给匿名函数
person = [
    {'name':'zs', 'age':19,'gender':'male'},
    {'name': 'z2', 'age': 29, 'gender': 'female'},
    {'name': 'zg', 'age': 39, 'gender': 'male'},
    {'name': 'zz', 'age': 59, 'gender': 'female'},
]
res = filter(lambda p : p['age'] > 35, person) # filter会遍历person，并将其中的每一项传给匿名函数
print(list(res))

# 过滤非法字符
names = ['zs', '', 'lis', None]
res = filter(lambda n: n, names) # 和下一句等价
# 方法2
res1 = filter(None, names) #特殊用法：当 filter 的第一个参数是 None 时，它会自动把可迭代对象中的每个元素当作布尔值判断，只保留那些“真值”（truthy）的元素。
# 方法3 列表推导式
res2 = [n for n in names if n] # 或者明确一点 [n for n in names if n not in (None, '') ]
print(list(res))
print(res2)

# sorted函数
# 1. 数字排序
nums = [20, 10, 40 ,33]
res = sorted(nums, reverse=True)
print(list(res))

# 2. 按照字符串的长度排序
names = ['python', 'sql', 'java']
res = sorted(names, key=lambda n: len(n))

ress = sorted(names) # 字符串默认按ascii码来排序
print(list(ress))

print(list(res))
print(ord('j'))
print(ord('s'))
print(ord('p'))

# 根据字典中的某个字段排序
rs = sorted(person, key = lambda p : p['age'])
print(list(rs))

# max min函数也可以用key参数
rs = max(person, key = lambda p : p['age'])
print(rs)
rs = min(person, key = lambda p : p['age'])
print(rs)

# reduce函数
from functools import reduce

# 数值统计
nums = [1, 2, 4, 6, 7]
resss = reduce(lambda x, y: x + y, nums)
print(resss)

# 字符串拼接
str_list = ['ab', 'cd', 'ef']
ress1 = reduce(lambda a, b: a+b, str_list)
print(ress1)

def summary(a, b):
    return a + b
res = reduce(summary, str_list) # reduce底层只会传2个参数给summary
print(res)