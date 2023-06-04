#import decimal;
#a = decimal.Decimal("3.0");
#b = decimal.Decimal("1.1");
#print(a-b);

#b = "yjnj123";
#print(b[:3].upper());
#print(f"name is {b}")
#a = "tst";
#b = "test";
#print("my name is {} and my {}" .format(a,b));

a = "The three primary Matrices in the ATT&CK framework are the Enterprise Matrix, The Mobile Matrix, And the ICS(Industrial Control System) Matrix.";
print(a);

for b in range(len(a)):
    #print(a[b]);
    if (a[b] == "M"):
        print("#M ==== ",a.index(a[b]));
    elif (a[b] == "a"):
        print("#a ==== ",a.index(a[b]));
    elif (a[b] == "t"):
        print("#t ==== ",a.index(a[b]));
    elif (a[b] == "r"):
        print("#r ==== ",a.index(a[b]));
    elif (a[b] == "i"):
        print("#i ==== ",a.index(a[b]));
    elif (a[b] == "c"):
        print("#c ==== ",a.index(a[b]));
    elif (a[b] == "e"):
        print("#e ==== ",a.index(a[b]));
    elif (a[b] == "s"):
        print("#s ==== ",a.index(a[b]));