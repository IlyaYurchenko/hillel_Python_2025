import string

usr_input = str(input('Enter string: \n'))

usr_input = ''.join(char for char in usr_input if char not in string.punctuation)

usr_input = usr_input.lower() and usr_input.title()
new_string = usr_input.replace(' ', '')


if len(new_string) > 140:
    new_string = new_string[:139] # +1 символ хештегу
    hashtag = f"#{new_string}"
else:
    hashtag = f"#{new_string}"

print(hashtag)



