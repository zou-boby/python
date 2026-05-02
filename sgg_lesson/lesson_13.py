"""
1. 标准多态
    要有继承
    要有方法重写
    要有类型限制
2. 鸭子多态
    没有👆三种限制，只关注功能，不注重限制
"""
class Animal:
    @staticmethod
    def speak():
        print('animal')

class Dog(Animal):
    def speak(self):
        print('dog')
class Cat(Animal):
    def speak(self):
        print('cat')

class Pig:
    def speak(self):
        print('pig')

def test(p: Animal):
    p.speak()

a = Animal()
b = Dog()
c = Cat()
d = Pig()
test(a)
test(b)
test(c)
test(d)

# 鸭子多态
# 即没有继承 也没有重写，也没有限制，只关注功能
class Person:
    def speak(self):
        print('person')

class Zw:
    def speak(self):
        print('zw')

def make_sound(p):
    p.speak()

p = Person()
z = Zw()
make_sound(p)
make_sound(z)