class Balloon():

    def __init__(self, pColour, pDefenceItem):
        self.__Health = 100 # INTEGER
        self.__Colour = pColour # STRING
        self.__DefenceItem = pDefenceItem # STRING

    def ChangeHealth(self, HealthChange):
        self.__Health = self.__Health + HealthChange
    
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False
        

userColour = str(input("Please enter a colour : ")) # STRING
userDefenceItem = str(input("Please enter a defence item : ")) # STRING
Balloon1 = Balloon(userColour, userDefenceItem) # Balloon

def Defend(balloonObj):

    opponentStrength = int(input("Please enter the strength of the opponent: ")) # INTEGER
    balloonObj.ChangeHealth(-opponentStrength) 
    print(f"Balloon object has {balloonObj.GetDefenceItem()} defence item")

    if balloonObj.CheckHealth() == True:
        print("Object has no health remaining!")
    else:
        print("Object still has health remaining!")

    return balloonObj

Defend(Balloon1)