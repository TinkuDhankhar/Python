l = []
while True:
    c=input('''
        1 push Element
        2 Pop Element
        3 Peek Element
        4 Display Element
        5 Exit
    ''')
    if c==1:
        n=input("Enter the values")
        l.append(n)
        print(l)
    elif c==2:
        if len(l) == 0:
            print("Empty Stack List")
        else:
            p = l.pop()
            print(p)
            print(l)
    elif c==3:
        if len(l) == 0:
            print("empty list")
        else:
            print("last list",l[-1])
    elif c==4:
        print("Display list",l)
    elif c==5:
        break;