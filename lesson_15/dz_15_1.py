class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

    def rec_square(self) -> float:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rectangle):
            return self.rec_square() == other.rec_square()
        return False

    def __add__(self, other: object) -> 'Rectangle':
        if isinstance(other, Rectangle):
            total_area = self.rec_square() + other.rec_square()
            return Rectangle(1, total_area)
        return NotImplemented

    def __mul__(self, n: float) -> 'Rectangle':
        if isinstance(n, (int, float)):
            new_area = self.rec_square() * n
            return Rectangle(1, new_area)
        return NotImplemented

    def __str__(self) -> str:
        return f'Rectangle({self.width}, {self.height})'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.rec_square() == 8, 'Test1'
assert r2.rec_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.rec_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.rec_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("OK")
