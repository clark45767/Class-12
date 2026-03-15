class Computer:
    def __init__(self):
      self.__maxprice = 900

    def sell(self):
       print("selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
       self.maxprice= price

c = Computer()
c.sell()

#change the price
c._maxprice = 1000
c.sell()

#using setter function
c.setMaxPrice(1000)
c.sell()