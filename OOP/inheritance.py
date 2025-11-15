# Inheritance - Used when there are multiple classes of repeating attributes
# Parent class - Super class
# Child class - subclass / derived class

class Animal():
    def __init__(self, pname):
        self._name = pname

    def makeSound(self):
        print("Some sound")
    
    # def get_name(self):
        # return self.__name
    
    # Only if it is private, we need to use a getter method


class Zebra(Animal):
    def __init__(self, pname, pstripeCount):

        Animal.__init__(self, pname) # MUST WRITE SELF
        # super().__init__(pname) # DO NOT USE SELF
        self.__stripeCount = pstripeCount

    def get_stripeCount(self):
        return self.__stripeCount
    
    def makeSound(self):
        # print(f" {self.__name} barks") # Overrides the makeSound method in the parent class. Does not work if it is in private
        print(self._name)

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
# Without the super() method, the dervied class methods will overwrite the methods inside the super class
# This principle is called overriding - methods in the child class overrides the methods in the parent class

Zebra1 = Zebra("Zoey", 20)
Zebra1.makeSound()
print(Zebra1.get_stripeCount())
