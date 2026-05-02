"""
1. 类的多重继承
2. 属性权限
    公有属性
    protected  _
    私有属性 __
3. getter setter
    通过装饰器实现
"""

class Person:
    max_age = 120
    def __init__(self, name, age, gender):
        self.name = name
        self.gender = gender
        self._age = age

    def speak(self, msg):
        print(f'{self.name} tell {msg}')

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < self.max_age:
            self._age = value
        else:
            print('修改失败！超过最大年龄')
class Worker:

    def __init__(self, company):
        self.company = company

    def showCompany(self):
        print(f'my company is {self.company}')

class Student(Person, Worker):
    def __init__(self, name, age, gender, company, stuId, grade):
       Person.__init__(self, name, age, gender)
       Worker.__init__(self, company)
       self.stuId = stuId
       self.grade = grade

    def showStudent(self):
        print(f'{self.name}, my company is {self.company}, 学号: {self.stuId}')
    def showAge(self):
        print(f'我的年龄{self._age}')

s1 = Student('xh', 12, 'male', 'ssss', '200002', 'xiaoxue')
s1.showStudent()

p1 = Person('ss', 12, 'male')
p1.speak('afaf')
s1.showAge()

p1.age = 100
print(p1.max_age)