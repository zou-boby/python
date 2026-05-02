"""
- 抽象类：不用做实例化，只作为父类 用于继承，让子类实现抽象方法
  - ``from abc import ABC, abstractmethod`` 先引入抽象类
  - 需要定义类继承自抽象类ABC
  - 需要定义抽象方法，用abstractmethod装饰器装饰
"""

from abc import ABC, abstractmethod
# 需要定义类继承自抽象类ABC
class Lesson(ABC):
    # 需要定义抽象方法，用abstractmethod装饰器装饰
    @abstractmethod
    def teach(self):
        pass
    # 定义普通方法
    def speak(self):
        print('ABC')

# l = Lesson() 无法实例化
# l.teach()

class Student(Lesson):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def teach(self):
        print('all lesson')

s = Student('zs', 11)
s.teach()