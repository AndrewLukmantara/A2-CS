class Item():
    
    # Initiliazing of attributes
    
    def __init__(self, pName, pPrice):
        self.__name = pName # type string
        self.__price = pPrice # type real
        
    # Getters
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    # Setters
    
    def set_name(self, newName):
        self.__name = newName
        
    def set_price(self, newPrice):
        self.__price = newPrice
        
    # Show item details
    
    def itemDetails(self):
        print(f"Name : {self.__name}\nPrice : {self.__price}")
        
class Cart():
    def __init__(self):
        self.__cartArr = [] # Array of type Item
        
    # Add items to the cart 
    
    def addItem(self, newItem):
        self.__cartArr.append(newItem)
    
    # Show cart details
    
    def showCartDetails(self):
        for item in self.__cartArr:
            print(item.get_name())
    
    # Calculate and return the total of prices in the cart
    
    def calculateTotal(self):
        sum = 0
        for item in self.__cartArr:
            sum = sum + item.get_price()
        return sum
    
# Creating a Cart

myCart = Cart()

# Create Item objects and add them to the Cart

myCart.addItem(Item("Apple", 2))
myCart.addItem(Item("Banana", 3))
myCart.addItem(Item("Orange", 4))
myCart.addItem(Item("Watermelon", 6))

# Showing the Cart details

myCart.showCartDetails()

# Showing the total price of the Cart

print(f"Total price of the cart : {myCart.calculateTotal()}")
