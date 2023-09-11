class Student(object):

    def __init__(self, student_id, student_name, student_sex):
        self.id = student_id
        self.name = student_name
        self.sex = student_sex


class StudentManagement(object):

    def __init__(self):
        self.student_list = []

    def addStudent(self, student):
        self.student_list.append(student)


if __name__ == '__main__':

    student_1 = Student(1001, '张三', '男')
    student_2 = Student(1002, '莉丝', '女')
    student_3 = Student(1003, '王武', '男')
    students = StudentManagement()
    students.addStudent(student_1)
    students.addStudent(student_2)
    students.addStudent(student_3)

    print('添加的学员信息：')
    for student in students.student_list:
        print(f'学号：{student.id}, 姓名：{student.name},性别：{student.sex}')
