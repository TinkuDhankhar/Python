# singal inharitanse
# multiply inharitanse
# multi level inharitance

class A:
    def disply(self):
        print("test")
class B(A):
    def display(self):
        print("B")
# Multiply 
class C(A,B):
    def displaya(self):
        print("Print c")
obj = B();
obj.disply()
obj.display()