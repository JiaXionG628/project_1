from functools import wraps


class Student(object):

    def __init__(self, student_id: int, student_name: str, student_sex: str):
        self.id = student_id
        self.name = student_name
        self.sex = student_sex

    def __repr__(self):
        return f'学号：{self.id}, 姓名：{self.name},性别：{self.sex}'


class MyException(Exception):
    def __init__(self, msg):
        print(f"添加学员参数 {msg} 有误")


class StudentManagement(object):

    def __init__(self):
        self.student_list = []

    def print_students_info(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            for student in self.student_list:
                print(student)
            return func

        return wrapper

    # @print_students_info
    def addStudent(self, student):
        # 添加学员
        self.student_list.append(student)
        print('添加成功，添加后的学员信息：', student)

    @print_students_info
    def deleteStudent(self, student_id: int):
        # 根据学号删除学员，查看所有学员信息
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)
                print('删除成功，删除的学员信息:', student)
                break
        else:
            print("未找到该学员")
        print("删除后的学员信息为：")

    def get_student_info_by_id(self, student_id: int):
        for student in self.student_list:
            if student.id == student_id:
                print("学员信息获取成功，该学员的信息为:")
                print(student)
                break
        else:
            print("学员不存在")

    @print_students_info
    def get_all_students_info(self):
        # 查询当前所有学员的信息
        return None

    def process_input(self, input_message):
        if input_message == 1:
            student_id = int(input("请输入想要查找的学员编号："))
            self.get_student_info_by_id(student_id)
            return 0
        elif input_message == 2:
            student_id = input("请输入学员编号：")
            if not student_id.isdigit():
                raise MyException('学员编号')
            student_name = input("请输入学员姓名：")
            student_sex = input("请输入学员性别：")
            if student_sex != '男' or student_sex != '女':
                raise MyException('学员性别')
            self.addStudent(Student(int(student_id), student_name, student_sex))
            return 0
        elif input_message == 3:
            student_id = int(input("请输入要删除的学员编号："))
            self.deleteStudent(student_id)
            return 0
        elif input_message == 4:
            self.get_all_students_info()
            return 0
        elif input_message == 5:
            print("成功退出系统，欢迎下次使用")
            return 1


if __name__ == '__main__':
    student_1 = Student(1001, '张三', '男')
    student_2 = Student(1002, '莉丝', '女')
    student_3 = Student(1003, '王武', '男')
    students = StudentManagement()
    students.addStudent(student_1)
    students.addStudent(student_2)
    students.addStudent(student_3)
    while True:
        print('--------欢迎来到学员信息管理系统--------')
        print('1.根据学号查看学员信息')
        print('2.添加学员')
        print('3.根据学号删除学员后，查看所有学员信息')
        print('4.查询当前所有学员的信息')
        print('5.退出系统')
        input_message = int(input('请输入你的选择：'))
        return_code = students.process_input(input_message)
        if return_code == 1:
            break
