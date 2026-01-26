class Vehicle():
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.__ID = ID # STRING 
        self.__MaxSpeed = int(MaxSpeed) # INTEGER
        self.__IncreaseAmount = int(IncreaseAmount) # INTEGER
        self.__HorizontalPosition = 0 # INTEGER
        self.__CurrentSpeed = 0 # INTEGER

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed
    
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    
    def GetHorizontalPosition(self):
        return self.__HorizontalPosition
    
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    
    def SetCurrentSpeed(self, CurrentSpeed): # CurrentSpeed : INTEGER
        self.__CurrentSpeed = int(CurrentSpeed)

    def SetHorizontalPosition(self, HorizontalPosition): # HorizontalPosition : INTEGER
        self.__HorizontalPosition = int(HorizontalPosition)

    def IncreaseSpeed(self):
        if self.__CurrentSpeed + self.__IncreaseAmount <= self.__MaxSpeed:
            self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
        else:
            print("Unable to do so")


class Helicopter(Vehicle):
    def __init__(self, ID , MaxSpeed, IncreaseAmount, VerticalChange, MaxHeight):
        self.__VerticalPosition = 0 # INTEGER
        self.__VerticalChange = int(VerticalChange) # INTEGER
        self.__MaxHeight = int(MaxHeight) # INTEGER
        super().__init__(ID, MaxSpeed, IncreaseAmount)

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):

        if (self.GetCurrentSpeed() + self.GetIncreaseAmount() <= self.GetMaxSpeed() and
            self.__VerticalPosition + self.__VerticalChange <= self.__MaxHeight):

            self.__VerticalPosition += self.__VerticalChange

            newSpeed = self.GetCurrentSpeed() + self.GetIncreaseAmount()
            self.SetCurrentSpeed(newSpeed)

            newHorizontal = self.GetHorizontalPosition() + self.GetCurrentSpeed()
            self.SetHorizontalPosition(newHorizontal)

        else:
            print("Unable to do so")



def outputVehicle(myVehicle):
    print(f"Horizontal Position : {myVehicle.GetHorizontalPosition()}")
    print(f"Speed : {myVehicle.GetCurrentSpeed()}")
    if isinstance(myVehicle, Helicopter):
        print(f"Vertical Position : {myVehicle.GetVerticalPosition()}")

myCar = Vehicle("Tiger", "100", "20") # myCar : Vehicle 
myHelicopter = Helicopter("Lion", "350", "40", "3", "100") # myHelicopter : Helicopter

myCar.IncreaseSpeed()
myCar.IncreaseSpeed()
outputVehicle(myCar)

myHelicopter.IncreaseSpeed()
myHelicopter.IncreaseSpeed()
outputVehicle(myHelicopter)