class test :
    a = 10
    def function(self):
        print(self.a);
    def showvalue(self):
        self.c = self.a * self.a;
        print(self.c);
    def __init__(self):
        print("this is constractor")
obj = test();
obj.function();
obj.showvalue();