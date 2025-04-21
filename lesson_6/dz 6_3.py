num = int(input("enter the digit: \n"))

while num > 10:
    digits = [int(digit) for digit in str(num)]
    num = 1
    for digit in digits:
        num *= digit

print(num)
