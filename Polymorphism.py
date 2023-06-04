# what is Polymorphism?
# Same name but different signature
class One:
    def NewFunction(self, name = ""):
        print("Hellow World"+" " + name)
class Two(One):
    def NewFunction(self):
        # call for One class function
        super().NewFunction()
        print("Testing world")

obj = Two()
obj.NewFunction()