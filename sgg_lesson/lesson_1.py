import math
"""
1. 注释
2. 变量

"""


name1 = 'hangman'
age1 = 22
name2 = 'sss'
age2 = 12
print('name1:%s, age1:%s, name2:%s, age2:%s'%(name1,age1,name2,age2))
name1, name2 = name2, name1
age1, age2 = age2, age1
print('name1:%s, age1:%s, name2:%s, age2:%s'%(name1,age1,name2,age2))

print(type(name1), type(age1))
print(isinstance(age1, str))

# num = int( input("输入数字:") )
# num1 = input("输入一个字符数字:")
# print(type(num), type(num1))


n1 = 0.1
n2 = 0.2
print(n1 + n2) # 由于底层是用补码存储，所以无法精确表示，存在精度丢失问题

print(round(n1 + 0.111, 2)) #  四舍五入

print(math.ceil(n1 + 0.111)) #  向上取整
print(math.floor(n1 + 0.111)) # 向下取整



"""
字符串
1. 创建
2. 运算
3. 字符串索引
"""
str1 = str()
str2 = "hello"
str3 = """me！
 hello world!
"""
print(str1, str2, str3)
print('-' * 20)
print(str3 + str2*2)

# 索引切片
print(str2[-1], str2[-2])
print("取连续的：%s" % str3[1:-1]) #  包头不包尾
print("隔着取: %s" % str2[0:6:2]) # 每隔2位取一个 不写默认是1
# 第一位起始默认位0 第二位结束位默认-1， 都可以省略
print("省略: %s" % str2[::2])

# 利用索引字符串反转
str4 = "hello world"
str4Rev = str4[::-1]
str4Rev1 = str4[-1:-12:-1]
print(str4Rev)
print("str4Rev1:",str4Rev1)

# 类型转换
str12 = 'ss12'
# print(int (str12)) 报错，无法转换®
str11 = "12.1"
print(float(str11))

print('*' * 20)
s1 = '' # 空串是False
i1 = 0  # False
s2 ='s' # 有内容是 True
print(bool(s1), bool(s2), bool(i1))

print( type (str(i1))) # int ---> str

print(str(True), type(str(True))) # bool ---> str
print(float(False))


a = '1a'
print(int(a, 16))  #  以16进制解读a

# 相同整数的地址问题
b = 4
c = 4
print(id(b), id(c))

d = 30001
e = 3000
print(id(d), id(e))

# 小作业
money = 100
money = money + 10
print(money)
money = money - 20
print("支付宝余额为 %d 元" % money)