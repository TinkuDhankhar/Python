print('''
    + add
    - minus
    / Devid
    * multiply
''')

num1 = int(input("value 1 "))
num2 = int(input("value 2 "))
opr = input("Oprator 1 ")
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1/num2)
else:
    print("Invalid format")