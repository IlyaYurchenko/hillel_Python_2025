import keyword
import string

usr_input = str(input('Enter the var name: \n'))
not_allowed = ['__', '___']

if usr_input[0] in not_allowed:
    print("False")
elif usr_input[0].isdigit():
    print('False')
elif usr_input in keyword.kwlist:
     print('False')
elif ' ' in usr_input:
    print('False')
elif any(char.isupper() or char in string.punctuation and char != '_' or usr_input.count('_') > 1 for char in usr_input):
    print('False')
else:
    print('True')
