from functools import wraps


class Student(object):

    def __init__(self, student_id: int, student_name: str, student_sex: str):
        self.id = student_id
        self.name = student_name
        self.sex = student_sex

    def __repr__(self):
        return f'学号：{self.id}, 姓名：{self.name},性别：{self.sex}'


class StudentManagement(object):

    def __init__(self):
        self.student_list = []

    def print_student_info(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            for student in self.student_list:
                print(student)
            return func

        return wrapper

    @print_student_info
    def addStudent(self, student):
        print('添加后的学员信息：')
        self.student_list.append(student)

    @print_student_info
    def deleteStudent(self, student_id: int):
        print("删除后的学员信息")
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)
                break
        else:
            print("未找到该学员")


if __name__ == '__main__':
    student_1 = Student(1001, '张三', '男')
    student_2 = Student(1002, '莉丝', '女')
    student_3 = Student(1003, '王武', '男')
    students = StudentManagement()
    students.addStudent(student_1)
    students.addStudent(student_2)
    students.addStudent(student_3)
    students.deleteStudent(1002)

    # for student in students.student_list:
    #     print(student)
