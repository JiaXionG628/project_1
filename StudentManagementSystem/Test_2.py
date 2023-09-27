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
        self.student_id = 1001
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
    def addStudent(self, student_name, student_sex):
        if student_sex != '男' and student_sex != '女':
            print('性别输入有误')
            return -1
        self.student_list.append(Student(self.student_id, student_name, student_sex))
        self.student_id += 1
        print('添加的学员信息：')
        return 0

    @print_student_info
    def deleteStudent(self, student_id: int):
        if not isinstance(student_id, int):
            print("删除的学号不是数字")
            return -1
        print("删除后的学员信息")
        for student in self.student_list:
            if student.id == student_id:
                self.student_list.remove(student)
                break
        else:
            print("输入学号不存在")
            return -1
        return 0


if __name__ == '__main__':
    students = StudentManagement()
    students.addStudent('张三', '男')
    students.addStudent('莉丝', '女')
    students.addStudent('王武', '男')
    students.deleteStudent('你好')

