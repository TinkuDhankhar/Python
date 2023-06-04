class Const :
    def __init__(self):
        self.__Name = "";
    def GetName(self):
        return self.__Name;
    def SetName(self, name):
        self.__Name = name

obj = Const()
obj.SetName("Hello World")
print(obj.GetName())