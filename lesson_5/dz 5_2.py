import keyword
import string

usr_input = str(input('Enter the var name: \n'))

if usr_input[0].isdigit():
    print('False')
elif usr_input in keyword.kwlist:
     print('False')
elif ' ' in usr_input:
    print('False')
elif usr_input.startswith('__') or usr_input.startswith('___'):
    print('False')
elif any(char.isupper() or char in string.punctuation and char != '_' for char in usr_input):
    print('False')
else:
    print('True')
