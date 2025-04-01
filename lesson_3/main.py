n1 = int(input("enter the first digit: "))
n2 = int(input("enter the second digit: "))
operator = int(input(" choose operator: \n [1] + \n [2] - \n [3] * \n [4] / \n"))

if operator == 1:
    result = n1 + n2
elif operator == 2:
    result = n1 - n2
elif operator == 3:
    result = n1 * n2
elif operator == 4:
    if n2 != 0:
        result = n1 / n2
    else:
        print("U can't subdivide by 0")
else:
    print("ERROR")

print(result)
