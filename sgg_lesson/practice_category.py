"""
1. 类的练习

学生管理系统
添加学生
删除学生
查看所有学生
录入成绩
退出

用到的知识：
继承
方法重写
类属性
装饰器
魔法方法 __str__
字符、列表、元组、字典的操作
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    stuId = 0
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        Student.stuId += 1
        self.stuId = f'{Student.stuId:03d}'
        self.scores = {}

    def updateScores(self, subject, scores):
        self.scores[subject] = scores

    def updateInfo(self, attr, val):
        setattr(self, attr, val)
    def __str__(self):
        # if self.scores:
        #     return f'学号：{self.stuId}-姓名：{self.name}-年龄：{self.age}-性别：{self.gender}-分数：{self.scores}'
        # else:
        #     return f'学号：{self.stuId}-姓名：{self.name}-年龄：{self.age}-性别：{self.gender}'
        score_part = f'-分数：{self.scores}' if self.scores else ''
        return f'学号：{self.stuId}-姓名：{self.name}-年龄：{self.age}-性别：{self.gender}{score_part}'
class Manager:
    stuList = []
    # 添加学生
    def add_stu(self ,name, age, gender, scores = None):
        stu = Student(name, age, gender)
        self.stuList.append(stu)
        if scores:
            self.update_scores(stu.stuId, scores)

    # 录入成绩
    def update_scores(self, stuId, scoresStr):
        for stu in self.stuList:
            if stu.stuId == stuId:
                # math-99,english-98
                scoresItem = scoresStr.replace('，', ',').split(',')
                for item in scoresItem:
                    subject, score = item.split('-')
                    stu.updateScores(subject, int(score))
                print('录入成功!')
                return
        print('录入失败！')

    # 删除学生
    def del_stu(self, stuId):
        for stu in self.stuList:
            if stu.stuId == stuId:
                self.stuList.remove(stu)
                print(f'{stu.name}的学生信息删除成功')
                return
        print('删除失败！请检查学生学号')

    # 查看所有学生
    def showAllStu(self):
        for stu in self.stuList:
            print(stu)
    @staticmethod
    def formatInfo(infoStr:str):
        baseInfo, *scores = infoStr.strip().replace('；', ',').split(';')
        if scores:
            return baseInfo, scores[0]
        else:
            return baseInfo
    # 开启面板
    def run(self):
        print('=======学生管理系统========\n1. 添加学生\n2.删除学生\n3. 显示所有学生信息\n4. 录入学生成绩\n5.退出')
        while True:
            num = input('请输入操作序号:')
            match (int(num)):
                case 1:
                    info = input('请输入要添加的学生信息:姓名-年龄-性别[;语文-50,数学-89]')
                    info = info.replace('；', ';')
                    info_1, *scores = info.split(';') # *scores会使得scores解包出来是 []类型，所以需要 scores = scores[0]
                    name, age, gender = info_1.split('-')
                    if scores:
                        scores = scores[0]
                        self.add_stu(name, age, gender, scores)
                    else:
                        self.add_stu(name, age, gender)
                case 2:
                    stuId = input('请输入要删除学生的学号:')
                    self.del_stu(stuId)
                case 3:
                    self.showAllStu()
                case 4:
                    infoStr = input('请输入要录入的学生成绩：学号;math-99,')
                    stuId, scores = infoStr.split(';')
                    self.update_scores(stuId, scores)
                case 5:
                    return

m = Manager()
m.run()

