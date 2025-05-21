class Human:
    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'First name: {self.first_name} \nLast Name: {self.last_name} \nAge: {self.age} \nGender: {self.gender}'

class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return super().__str__() + f'\nRecord Book: {self.record_book}'

class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student):
        if len(self.group) >= 10:
            raise GroupIsFull()
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

class GroupIsFull(Exception):
    def __init__(self, message = 'The group is full'):
        super().__init__(message)

gr = Group('PD1')

for i in range(10):
    student = Student('Male', 20 + i, f'Name{i}', f'LastName{i}', f'RB{i}')
    gr.add_student(student)

try:
    gr.add_student(Student('Female', 22, 'Extra', 'Student', 'RB999'))
except GroupIsFull as e:
    print(e)

#
# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
#
#
# gr.add_student(st1)
# gr.add_student(st2)
#
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'
#
# gr.delete_student('Taylor')
# print(gr) # Only one student
#
# gr.delete_student('Taylor') # No error!
