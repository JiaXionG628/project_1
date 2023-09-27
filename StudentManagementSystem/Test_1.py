class Student(object):

    def __init__(self, student_id, student_name, student_sex):
        self.id = student_id
        self.name = student_name
        self.sex = student_sex

    def __repr__(self):
        return f'学号：{self.id}, 姓名：{self.name}, 性别：{self.sex}'


class StudentManagement(object):

    def __init__(self):
        self.student_id = 1001
        self.student_list = []

    def addStudent(self, student_name, student_sex):
        if student_sex != '男' and student_sex != '女':
            print('性别输入有误')
            return -1
        self.student_list.append(Student(self.student_id, student_name, student_sex))
        self.student_id += 1
        return 0


if __name__ == '__main__':
    students = StudentManagement()
    students.addStudent('张三', '男')
    students.addStudent('莉丝', '女')
    students.addStudent('王武', '男')
    print('添加的学员信息：')
    for student in students.student_list:
        print(student)
