class Subdivide:
    def subdiv(self, number: int) -> int:
        return number % 2 == 0

result = Subdivide()

def is_even(number: int) -> bool:
    return result.subdiv(number)

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
