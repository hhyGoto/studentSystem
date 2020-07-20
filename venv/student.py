"""
******************************
欢迎使用学生管理系统
    1.显示所有学生
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.退出系统
*******************************
"""
from datetime import datetime

#模拟学生数据
data = [
    {
        'name' : 'Tom',
        'sex' : '男',
        'birthday' : '200002'
    },
    {
        'name' : 'Tomy',
        'sex' : '男',
        'birthday' : '201002'
    },
    {
        'name' : 'huang',
        'sex' : '男',
        'birthday' : '200102'
    },
    {
        'name' : 'ying',
        'sex' : '女',
        'birthday' : '202002'
    }
]

#学生
class Student :
    def __init__(self,name,sex,birthday):
        self.name = name
        self.sex = sex
        self.birthday =birthday

    def get_age(self):
        age = int(datetime.now().year) -int(self.birthday[:4])
        return age

class StudentSystem:
    def __init__(self, name):
        self.name = name
        self.data = []

    #加载数据
    def load_data(self):
        for item in data :
            student = Student(item['name'],item['sex'],item['birthday'])
            self.data.append(student)
    #启动学生管理系统
    def start(self):
        self.load_data()
        self.show_menu()
        while True:
            op = input("选择操作:")
            if op == '1':
                self.show_all_student()
            if op =='2':
                self.add_student()
            if op == '3':
                self.show_student()
            if op == '4':
                self.edit_student()
            if op == '5':
                print("退出系统")
                break
    # 显示菜单
    def show_menu(self):
        print(f"""
        ******************************
        欢迎使用{self.name}
            1.显示所有学生
            2.新建学生信息
            3.查询学生信息
            4.修改学生信息
            6.退出系统
        *******************************
        """)
    #美化输出
    def beauty_print(self,data_list):
        for index,student in enumerate(data_list):
            print(f"序号:{index}", end='\t')
            print(f"姓名:{student.name}", end='\t')
            print(f"性别:{student.sex}", end='\t')
            print(f"年龄:{student.get_age()}")

    #显示所有学生
    def show_all_student(self):
        self.beauty_print(self.data)

    #显示学生
    def show_student(self):
        name = input("输入查询姓名:")
        for student in self.data:
            if student.name == name:
                self.beauty_print([student])

    #新建学生信息
    def add_student(self):
        name=input("请输入姓名:")
        sex=input("请输入性别:")
        birthday=input("请输入生日:")
        student = Student(name,sex,birthday)
        self.data.append(student)

    #修改学生信息
    def edit_student(self):
        name1 = input("输入修改的姓名:")
        for student in self.data:
            if student.name == name1:
                self.beauty_print([student])
                break
        else:
            print("学生不存在")
            name1 = input("输入修改的姓名:")

        name2 = input("请输入新姓名:")
        sex = input("请输入新性别:")
        birthday = input("请输入新生日:")
        student = Student(name2, sex, birthday)
        for index,s in enumerate(self.data):
            if s.name == name1:
                self.data[index]=student

if __name__ == '__main__' :
    student_sys = StudentSystem('学生管理系统')
    student_sys.start()
