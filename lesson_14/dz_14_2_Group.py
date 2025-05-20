from dz_14_2_Student import *

class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) >= 10:
            raise ValueError('10 students limit')
        self.group.add(student)

    def find_student(self, last_name: str) -> Student | None:
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name: str):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)
            print(f'Student {last_name} removed')
        else:
            print(f'Student {last_name} not found in the group.')

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Group number: {self.number}\nStudents:\n{all_students}'
