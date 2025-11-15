class Item():
    def __init__(self, Iname, Iprice):
        self.__name = Iname
        self.__price = Iprice
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

    def set_name(self, newName):
        self.__name = newName
    
    def set_price(self, newPrice):
        self.__price = newPrice


class Cart():
    def __init__(self):
        self.__cart = [] # Items of type Item

        # Whenever a class has a reference to another class, it is called containment / aggregation
    
    def addItem(self, item):
        self.__cart.append(item)

    def calculateTotal(self):
        sum = 0
        for i in self.__cart:
            sum = sum + i.get_price()
        return sum
        

# Item1 = Item("Apple", 40)
# Item2 = Item("Banana", 60)
# Item3 = Item("Orange", 70)
# Item4 = Item("Dragon Fruit", 90)

# myCart = Cart()
# myCart.addItem(Item1)
# myCart.addItem(Item2)
# print(myCart.calculateTotal())

myCart = Cart()

myCart.addItem(Item("Apple", 40))
myCart.addItem(Item("Banana", 60))
myCart.addItem(Item("Orange", 70))
myCart.addItem(Item("Dragon Fruit", 90))
print(myCart.calculateTotal())
