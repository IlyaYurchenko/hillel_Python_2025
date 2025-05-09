import string

usr_input = str(input("enter letter diapazone: "))

start, end = usr_input.split('-')
start_index = string.ascii_letters.index(start)
end_index = string.ascii_letters.index(end)

print(string.ascii_letters[start_index:end_index+1])