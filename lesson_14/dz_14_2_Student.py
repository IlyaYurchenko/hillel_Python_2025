from dz_14_2_Human import Human


class Student(Human):
    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return super().__str__() + f'\nRecord Book: {self.record_book}'

    def __eq__(self, other) -> bool:
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))



