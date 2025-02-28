class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print((self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

#Changing the Price
c.__maxprice = 1000
c.sell()

#Setting the Price
c.setMaxPrice(1000)
c.sell()