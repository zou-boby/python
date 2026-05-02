"""
1. 魔法方法----在特定场景自动调用的方法
    __len__
    __str__
    __lt__
    __eq__
    __ne____

    由于实例对象 这种类型没有原始的len方法，或者说实例对象无法使用原始的len方法，会报错，所以需要重写一下

"""


class Person:
    max_age = 120
    def __init__(self, name, age, gender, Id):
        self.name = name
        self.age = age
        self.gender = gender
        self.__id = Id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    # 在print(p1) 或者 str(p1) 时会自动调用__str__
    def __str__(self):
        return {
                'name': self.name,
                'age': self.age,
                'gender': self.gender,
            }.__str__()

    # 在调用len(p1)时自动调用
    def __len__(self):
        return len(self.__dict__)
    # p1 < p2 时自动调用
    def __lt__(self, other):
        return self.age < other.age
    # p1 > p2时自动调用
    def __gt__(self, other):
        return self.age > other.age
    # 原来调用p3 == p2时通过内存中的地址来比较的，现在改写后通过属性来判断
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # 在p1.name 访问属性时自动调用  或者 在访问不存在的属性时自动调用
    def __getattr__(self, item):
        # if item in self.__dict__:
        #     return self.item
        # else:
        #     print(f'{item}不存在')
        #     return None

        return f'{item}属性不存在'

p1 = Person('张三', 19, 'male', 1)
p2 = Person('李四', 24, 'female', 2)
p3 = Person('李四', 24, 'female', 2)
# 原理： eg： print(p1) 首先会去调用p1.__str__()方法，如果没有就去Person中找，然后去object中找

# print(p1)
# print(p2)
#
# print(len(p1))
# print(p1 < p2)

print(p3 == p2)

print(p1.name)


print(issubclass(Person, object))
print(issubclass(int, object))
# for k in object.__dict__:
#     print(k)
print(dir(p1))