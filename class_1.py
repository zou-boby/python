from sys import flags

a=21
b=10
c=a+b
print(c)
d=a//b

name="zhangsan"
print(name[1:4]) #从1号位开始读取 到4-1号位结束
print(name[1::2]) #从1号位开始，每隔2个进行读取
print(name[:5])
print(name[1:-1]) # 从后往前 从-1开始

# 字符串的拼接
first_name="张"
last_name="三"
print(first_name+last_name)
print(first_name*2+last_name)
print(first_name+"10")
print("\n")
name1=input("输入姓名：")
try:
    score=float( input("输入分数：") ) # 强制转化为float类型
    s="姓名：%s, 分数：%.2f"
    print(s % (name1, score))
except ValueError:
    print("输入错误，请输入数字！")


