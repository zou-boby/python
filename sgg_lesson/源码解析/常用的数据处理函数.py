"""
1. reduce
    def reduce(function, iterable, /, initial=initial_missing):
        it = iter(iterable)
        if initial is initial_missing:
            value = next(it)
        else:
            value = initial
        for element in it:
            value = function(value, element)
        return value

    2. next(iterator, default=None)
"""

_initial_missing = object()
"""reduce
object() 返回一个object基类的实例对象
一个特殊的哨兵值： 为了判断 传入的是None还是没有传值
"""
def reduce(function, iterable, /, initial=_initial_missing): # 限制传参： 在 / 前只能用位置参数
    it = iter(iterable) # 将参数iterable 转化成迭代器 __iter__魔法方法
    if initial is _initial_missing:
        value = next(it) # __next__ 获取迭代器中的下一个数据
    else:
        value = initial # 初始值
    for element in it:
        value = function(value, element) # 规定了function只能是2个参数
    return value
rs = reduce(lambda x, y: x+y, range(10), 20)
print(rs)

"""next ： __next__
    iter: __iter__

"""
def next(iterator, default = None):
    try:
        return iterator.__next__()
    except StopIteration: # 捕获 StopIteration异常，即没有下一个元素了
        if default is not None:
            return default
    raise # 重新抛出捕获的异常


class MyRange:
    current = 0
    def __init__(self, data):
        self.data = data
        self.start = 0
        self.end = len(data)
    def __iter__(self):
        # return self 最简单的实现，因为类本身就是迭代器
        # return iter(self.data)
        for i in range(self.start, self.end):
            yield self.data[i]
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.data[self.current]
        self.current += 1
        return val

m1 = MyRange([1, 3, 4, 5])
nx = next(m1) # 1
nx = next(m1) # 3
nx = next(m1) # 4
print(nx)

mIt = iter(MyRange((9, 8, 7, 6)))
print(next(mIt))
print(next(mIt))
