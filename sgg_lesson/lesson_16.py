"""
5. 高阶函数
- 定义： 参数或者返回值是函数
- 意义：
  - 代码复用性高，可以把行为独立出去，传入不同的函数实现不同的逻辑
  - 函数更灵活通用
  - 高阶函数是装饰器和闭包的基础


6. 条件表达式 [三目运算符】
7. 匿名函数
  - 只能写一行，不能写多行
  - 不能写代码块 if for while
  - 冒号右边必须是表达式，而且只能写一个表达式
  - 表达式会自动作为返回值
"""

def info(msg):
    print(msg)
def warn(msg):
    print(msg)
def error(msg):
    print(msg)
def log(func, msg):
    return func(msg)
log(info, 'ssaf')


# 三目运算符 val1 if 条件 else val2

age = 18
# if age >= 18:
#     print('成年')
# else:
#     print('未成年')

text = '成年' if age >= 18 else '未成年'
print(text)

# 匿名函数
add1 = lambda x, y: x + y
add2 = lambda x: x + 2
add3 = lambda : 'safaf'

print(add1(1, 2))
print(add2(23))
print(add3())

def calc(func, *args):
    return func(*args)

res = calc(lambda x, y: x + y, 10, 20)
print(res)
