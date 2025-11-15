class Passenger():
    
    #  Initiliazing of attributes
    
    def __init__(self, pName, pPassportNum):
        self.__name = pName # type string
        self.__passportNumber = pPassportNum # type string
        
    # Getters
    
    def get_name(self):
        return self.__name
    
    def get_passportNumber(self):
        return self.__passportNumber
    
    # Setters
    
    def set_name(self, newName):
        self.__name = newName
    
    def set_passportNumber(self, newPassportNum):
        self.__passportNumber = newPassportNum
    
    # Shows passenger details
    
    def passengerDetails(self):
         print(f"Name : {self.__name}\nPassport Number : {self.__passportNumber}")
        
class Flight():
    
    #  Initiliazing of attributes
    
    def __init__(self):
        self.__flightArr = [] # Array of type Passenger
    
    # Adding passengers
    
    def addPassenger(self, newPassenger):
        self.__flightArr.append(newPassenger)
    
    # Displaying passengers
    
    def displayPassenger(self):
        for passenger in self.__flightArr:
            print(passenger.get_name())
            
# Create passenger objects
p1 = Passenger("Alice", "P12345")
p2 = Passenger("Bob", "P67890")
p3 = Passenger("Charlie", "P24680")
p4 = Passenger("John", "P67679")

# Create a flight
myFlight = Flight()

# Add passengers to the flight
myFlight.addPassenger(p1)
myFlight.addPassenger(p2)
myFlight.addPassenger(p3)
myFlight.addPassenger(p4)

# Display all passengers
myFlight.displayPassenger()