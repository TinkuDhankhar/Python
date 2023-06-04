# Input1 = eval(input("Enter your first value "));
# Input2 = eval(input("Enter your secound Value "));
# Intrest = eval(input("Enter Intrest amount"));
# Time = int(input("Enter Your Time"));
# print((Input1*Input2*Intrest*Time)/100);
# Find Last Digit number
# UserInput = eval(input("Enter you number"));
# ld = UserInput%10;
# print("Last Digit Number :", ld);

# Input1 = int(input("Enter your first value : "));
# Input2 = int(input("Enter your secound value : "));
# Input3 = input("Enter Your Action : ");
#
# if Input3 == '+':
#     print(Input1 + Input2);
# elif Input3 == '-':
#     print(Input1 - Input2);
# elif Input3 == '*':
#     print(Input1 * Input2);
# else:
#     print("No action executed");
# Input1 = int(input("Enter number of the tickets"));
# Input2 = input("Enter Your type of seat");
# Input3 = input("Enter Your Booking Type : ");
#
# if Input2.lower() == "ordinary":
#     if Input3.lower() == "online":
#         print(Input1*(int("2500")) / 0.10)
#     elif Input3.lower() == "advance booking":
#         print(Input1*(int("2500")) / 0.8)
#     elif Input3.lower() == "ticket window":
#         print(int("2500"))
# elif Input2.lower() == "pavilion":
#     if Input3.lower() == "online":
#         print(int("3500")/10)
#     elif Input3.lower() == "advance booking":
#         print(int("3500")/8)
#     elif Input3.lower() == "ticket window":
#         print(int("3500"))
# elif Input2.lower() == "upper pavilion":
#     if Input3.lower() == "online":
#         print(int("4500")/10)
#     elif Input3.lower() == "advance booking":
#         print(int("4500")/8)
#     elif Input3.lower() == "ticket window":
#         print(int("4500"))
# elif Input2.lower() == "commentary box":
#     if Input3.lower() == "online":
#         print(int("6000")/10)
#     elif Input3.lower() == "advance booking":
#         print(int("6000")/8)
#     elif Input3.lower() == "ticket window":
#         print(int("6000"))
# elif Input2.lower() == "vip":
#     if Input3.lower() == "online":
#         print(int("8000")/10)
#     elif Input3.lower() == "advance booking":
#         print(int("8000")/8)
#     elif Input3.lower() == "ticket window":
#         print(int("8000"))

# Input = input("Enter your value : ");
# if Input == 'A' or Input == 'a':
#     print(Input, "Is vowel");
# elif Input == 'E' or Input == 'e':
#     print(Input, "Is vowel");
# elif Input == 'i' or Input == 'I':
#     print(Input, "Is vowel");
# elif Input == 'O' or Input == 'o':
#     print(Input, "Is vowel");
# elif Input == 'u' or Input == 'U':
#     print(Input, "Is vowel");
# else:
#     print(Input, "Is Consonant");

# ls = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# if Input in ls:
#     print(Input, "Vowel");
# else:
#     print(Input, "Consonant")
i = 5
sum = 0
while i <= 10:
    a = int(input("Enter your value : "))
    sum +=a
    i +=1
print("result",sum)