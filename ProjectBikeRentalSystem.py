class BikeShop:
    def __init__(self, Stock):
        self.Stock = Stock
    def DisplayBikes(self):
        print("Total Bikes", self.Stock)
    def RentForBike(self,qty):
        if qty <= 0:
            print("Enter positive value or greater then zero")
        elif self.Stock == 0:
            print("Stock not available", self.Stock)
        elif qty > self.Stock:
            print("Enter the value (less then stock)")
        else:
            self.Stock = self.Stock - qty
            print("Total Prices", qty*100)
            print("Total bikes", self.Stock)
obj = BikeShop(100)
while True:
    ci = int(input('''
1. Display Stock
2. Rent an Bikes  
3. Exit
    '''))
    if ci == 1:
        obj.DisplayBikes()
    elif ci == 2:
        val = int(input('Enter your QTY : --- '))
        obj.RentForBike(val)
    else:
        break
