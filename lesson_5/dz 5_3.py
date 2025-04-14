
usr_input = str(input('Enter string: \n'))
j = 0

usr_input = usr_input.lower() and usr_input.title()
new_string = usr_input.replace(' ', '')

if len(new_string) > 140:
    new_string = new_string[:139] # +1 символ хештегу
    hashtag = f"#{new_string}"
else:
    hashtag = f"#{new_string}"

print(hashtag)


