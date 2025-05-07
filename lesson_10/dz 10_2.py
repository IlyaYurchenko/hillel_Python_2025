import string

def first_word(text):
    """ Пошук першого слова """
    text = text.lstrip(string.punctuation + ' ')
    new_lst = text.split()
    first_word = new_lst[0]
    for word in text:
        if '.' in word:
            new_lst = text.split('.')
            first_word = new_lst[0].strip(string.punctuation)
        else:
            first_word = new_lst[0].strip(string.punctuation + ' ')
        new_lst = text.split()
        first_word = new_lst[0]
    print(first_word)

    return first_word

first_word(".., and so on ...")

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')