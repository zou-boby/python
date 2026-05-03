"""
- 函数进阶
1. 函数是function类的实例化对象
2. 函数可以赋值给变量以及可以添加属性 ![img_5.png](img_5.png)
3. 可变参数和不可变参数
   - 不可变参数![img_4.png](img_4.png)
   - 可变参数![img_6.png](img_6.png)
4. 函数可以作为参数或者返回值

"""
# 函数是function类的实例化对象
def speak():
    print('sss')

print(type(speak)) # <class 'function'>
# 给函数添加属性
speak.desc = '这是说话函数'
print(speak.desc)
# 把函数赋值给变量
pron = speak
print(pron.desc)
pron()


# 可变参数[list, dict, set]和不可变参数 int,str, tuple
# 不可变参数
a = 1
def hello(message):
    message = 3
    print(message)
hello(a)
print(a)

# 可变参数
l1 = [10, 20 ,30]
def print_list(l):
    print(l)
    l[0] = 33
    print(l)
print_list(l1)
print(l1)

# 函数可以作为参数或者返回值
#函数做参数
def h():
    print('hello')
def wellow(h):
    print('wellow')
    h()
wellow(h)
# 函数做返回值
def a():
    print('a')
    def show(msg):
        print(f'show {msg}')
    return show
a()('你好')
show = a()
show('hello')


