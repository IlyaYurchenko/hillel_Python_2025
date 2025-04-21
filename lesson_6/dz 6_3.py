num = int(input("enter the digit: \n"))

while num >= 10:
    digits = [int(digit) for digit in str(num)]
    for digit in digits:
        num = 1
        num *= digit

print(num)
