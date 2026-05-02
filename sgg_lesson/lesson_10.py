"""
1. 类

"""

from datetime import datetime
class Person:
    # 类属性: 通常保存公共数据，是类和每个实例都可以访问的
    planet = '地球'
    max_age = 120
    # init初始化方法，给当前正在创建的实例添加属性【实例属性时每个实例单独拥有的】，在创建实例时，会自动调用init方法
    def __init__(self, name, age):
        self.name = name
        if age <= 120:
            self.age = age
        else:
            print(f'年龄超出，将设置为最大值:{Person.max_age}')

    # 实例方法 --- 供实例调用的
    def speak(self, message):
        print(f'{self.name} says {message}')
    def run(self, distance):
        print(f'{self.name} runs {distance} miles')

    """
    @classmethod 装饰器： 通过这个装饰器定义的就是类方法
    类方法的参数： cls类本身，以及自定义参数
    有了cls参数就可以访问类的相关属性和方法
    类方法通常用于实现类相关的逻辑 eg： 操作类一级的信息、一些工厂方法
    """
    @classmethod
    def create(cls, msg):
        name, year = msg.split('-')
        cur_year = datetime.now().year
        age = cur_year - int(year)
        return cls(name, age)
    @classmethod
    def change_planet(cls, val): # 操作类一级的信息
        cls.planet = val

    """
    @staticmethod 静态方法装饰器
    通常用于定义与类相关的工具方法
    这类方法可以通过实例调用：但不推荐，其他语言会报错
    """
    @staticmethod
    def is_adult(year):
        cur_year = datetime.now().year
        if cur_year - int(year) >= 18:
            return True
        else:
            return False

print(Person.__dict__)

P1 = Person('张三', 12)
P2 = Person('张三12', 23)

print(P1.name, P1.age, P1.planet)
print(P2.name, P2.age, P2.planet)
print(P1.__dict__)
print(P2.__dict__)


print(type(P1))

P1.speak('垃圾🗑️')
def speak():
    print('sfafas')
P2.speak = speak
P2.speak()


p3 = Person('李四', 130)
print(p3.name, p3.max_age)
p3.age = 122
print(p3.name, p3.age)
p3.run(100)
Person.run(p3, 200) # 通过类来调用实例方法，不推荐

Person.change_planet('月球')
p4 = Person('ss', 22)
print(p4.planet)

# 通过类方法 create来创建实例对象
p5 = Person.create('zjr-2000')
print(p5.__dict__)



# 继承
"""
Person是父类、超类， student是子类
调用方法和属性时在继承链上的体现：子类 ----> 父类
"""
class Student(Person):
    def __init__(self, name, age, stuId, grade):
        # 调用父类的初始化方法的 2 种方式
        super().__init__(name, age) # 推荐第一种
        # Person.__init__(self, name, age) # 第二种
        self.stuId = stuId
        self.grade = grade


    # 方法重写 -- 子类中定义了和父类相同的方法
    def speak(self, message):
        print(f'学生叫{self.name}，学号:{self.stuId}, 年级：{self.grade} 我想说 {message}')


s1 = Student('小花', 18, '20260901', '研一')
print(s1.__dict__)

s1.speak('测试重写方法')


print(isinstance(s1, Student))
print(isinstance(s1, Person))
print(issubclass(Student, Person))
print(issubclass(Person, Student))




