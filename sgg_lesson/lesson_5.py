"""
字符串的方法

对于字符串和元组都是不可改变类型，所以 对于二者的对应方法并不会改变原来的对象，而是生成一个新的对象
"""
iStr = 'hello world'
# find 返回所找元素的索引
res = iStr.find('o', 5, -1)
print(res)
# count 返回查找元素的个数
res = iStr.count('o', 5, -1)
print(res)
# index 返回查找元素的第一个所在的索引下标
res = iStr.index('o', 0, -1)
print(res)
# join 用# 来拼接字符串中的各个元素
print('#'.join(iStr))
# islower 判断是否是小写 isupper 判断是否为大写
print(iStr.islower())
print(iStr.isupper())
# isdigit 判断是不是数字 isalpha 判断是不是字母 isalunm 判断是否只有数字或字母
print('123'.isdigit())

# format
"""
1. 格式化输出
2. 对齐
3. 进制转换
"""
name = 'xiaa'
age = 12
print("姓名：{}, 年龄:{}".format(name, age))
print("姓名: {1}, 年龄: {0}".format(age, name))
print("姓名: {name}, 年龄: {age}".format(name = 'hangman', age = 23)) # 指定填充®
print(f"姓名: {name}, 年龄：{age}") # 简洁写法

# 对齐
print("{:>5}".format(123))
print("{:<5}".format(123))
print("{:*>5}".format(123))
print("{:,}".format(1000000)) # 千分位分隔符
# 进制转换
print("{:x}".format(255)) # 十六进制输出
print("{:#x}".format(255)) # 十六进制输出
print("{:#b}".format(10)) # 八进制输出

# capitalize() 将第一个改成大写，其他改成小写
print(iStr.capitalize()) # 生成一个新的字符串对象
print(iStr) # 所以这里输出的还是原来的对象
# 除非这样
iStr = iStr.capitalize()
print(iStr)
