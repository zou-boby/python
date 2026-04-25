name = '章三'
age = 12
score = 67.56
print("%4.2s" %name)
print("%6.1f" %score)

print("1232\t43".expandtabs(8)) # 设置制表符为8位
print("122\t11".expandtabs(8))

print(f"姓名：{name}, 年龄: {age}, 分数: {score}")


def showSelfInfo(name, age, score):
    print(f"姓名:{name} 年龄:{age} 分数:{score}")

showSelfInfo('李四', 12, 711)

# showSelfInfo(name='李四', 12, score=711) # 位置参数必须在关键字参数之前

# 限制参数
def greet(name, /, age, company, *, city='jiangxi'):
    print(f"name={name}, age={age}, company={company}, city={city}")

greet('张三', 12, company='sfaf')
greet('张三', 12, 'sfaf', city='sss')


# 可变参数
# *args 可变位置参数。**kwargs 可变关键字参数
def testVariablePara(name, *args, **kwargs):
    print(f"name={name}, info={args}, place={kwargs}")
testVariablePara('张三', 12, 733, country='China', city='jiangxi')

# None
msg = None

# 全局作用域和局部作用域
info = {
    'name': 'zhangsan',
    'age': 21,
}
a, b = 1, 2
def testScope():
    country = 'China'
    city = 'jiangxi'
    print(f"country={country}, city={city}, info.name={info['name']}, info.age={info['age']}")
    global a, b # 声明全局的 a b，此后a b就是全局变量
    a, b = 3, 4 # 直接修改全局的a b

    print(f"a={a}, b={b}")

testScope()
print(f"a={a}, b={b}")

# 局部作用域和局部变量会在函数调用是创建，函数执行结束时销毁
num = 0
def testNumAdd():
    global num
    num += 1
    print(f"num={num}")

testNumAdd()
testNumAdd()


# 函数的嵌套
def testFuncNested():
    test1()

def test1():
    print("------进入test1------")
    test2()
    print("------退出test1------")

def test2():
    print("------进入test2------")
    test3()
    print("------退出test2------")

def test3():
    print("------进入test3------")
    print("------正在执行test3------")
    print("------退出test3------")

testFuncNested()
"""
1. 函数的定义不会执行函数体中的代码，只有在函数执行时才会执行
    所以在testFuncNested()函数执行时才会去看内部的代码，此时所有的函数都以及定义了，所以可以正常执行
2. 结果
------进入test1------
------进入test2------
------进入test3------
------正在执行test3------
------退出test3------
------退出test2------
------退出test1------
原理就是： 函数调用栈
"""


# 函数的说明文档
def testFuncDoc(n1, n2, n3):
    """
    测试函数的说明文档
    :param n1: 参数1
    :param n2: 参数2
    :param n3: 参数3
    :return: 返回参数的和
    """
    return n1 + n2 + n3
res = testFuncDoc(1, 2, 3)
print(f"testFuncDoc result: {res}")



# 函数的应用: 项目比赛
def totalNum(nums):
    return sum(nums)

def average(total, days):
    return total / days

def checkSuccess(total, aver, goal = 140):
    return total >= goal and aver >= 60

def main(project, duration = 7):
    print(f'【{project}{duration}天挑战赛开始！！！】')
    nums = []
    for i in range(duration):
        temp = input(f'请输入第{i+1}天的记录:')
        nums.append(int(temp))
    total = totalNum(nums)
    aver = average(total, duration)
    if checkSuccess(total, aver):
        print('挑战成功!!!')
    else:
        print('挑战失败！！！')


# main('俯卧撑', 3)


