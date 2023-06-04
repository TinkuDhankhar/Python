# Overloading and Overriding
# Overloading
class Area:
    def find_area(self, X = None, Y = None):
        if X != None and Y != None:
            print(X, Y)
        elif X != None:
            print(X * X)
        elif Y != None:
            print(Y + Y)
        else:
            print(f"Nothing pass X and Y Value")
# create class Object
obj = Area()
obj.find_area()
obj.find_area(10)
obj.find_area(X=None, Y=100)
# Overriding
class A:
    def Function(self):
        print("Class A")
class B(A):
    def Function(self):
        print("Class B")
obj = B()
obj.Function();