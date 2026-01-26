class Plane():

    def __init__(self, pOrigin, pDestination, pFlightID, pDuration):
        self.__Origin = pOrigin
        self.__Destination = pDestination
        self.__FlightID = pFlightID
        self.__Duration = int(pDuration)
        self.__Airline = "Monkey Flight"
        self.__Capacity = 100

    def GetOrigin(self):
        return self.__Origin
    
    def GetDestination(self):
        return self.__Destination
    
    def GetFlightID(self):
        return self.__FlightID
    
    def PrintDetails(self):
        print(f"Flight No : {self.__FlightID} from : {self.__Origin} to : {self.__Destination} has a duration : {self.__Duration}")    


class Passenger(Plane):
    def __init__(self, pName, pID, pOccupation, pOrigin, pDestination, pFlightID, pDuration):
        self.__Name = pName
        self.__ID = pID
        self.__Occupation = pOccupation
        super().__init__(pOrigin, pDestination, pFlightID, pDuration)

    def GetName(self):
        return self.__Name
    
    def GetID(self):
        return self.__ID
    
    def PrintPassengerDetails(self):
        print(f"Passenger Name : {self.__Name}\nPassengerID : {self.__ID}\nFlight ID : {self.GetFlightID()}")
        print(f"Occupation : {self.__Occupation.GetOccName()}")
    

class Occupation():
    def __init__(self, pOccName, pMeanSalary):
        self.__OccName = pOccName
        self.__MeanSalary = float(pMeanSalary)

    def GetSalary(self):
        return self.__MeanSalary
    
    def GetOccName(self):
        return self.__OccName
    

    

Occupation1 = Occupation("Miner", 1000)
Passenger1 = Passenger("Andrew", "X39087", Occupation1, "Jakarta", "Bali", "0273", 2)
print(Passenger1.GetFlightID())
Passenger1.PrintDetails()
Passenger1.PrintPassengerDetails()
