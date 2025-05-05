class New_class:
    def divide(self, number):
        return number % 2 == 0

result = New_class()

def is_even(number):
    return result.divide(number)

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('OK')
