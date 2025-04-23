import string

text = 'A man, a plan, a canal: Panama'
def is_palindrome(text: str) -> bool:
    check_text = text.replace(" ", "").lower()
    for char in check_text:
        if char in string.punctuation:
            check_text = check_text.replace(char, '')

    if check_text == check_text[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")