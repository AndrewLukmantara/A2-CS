class Character():
    def __init__(self, pName, pX, pY):
        self.__Name = pName # STRING
        self.__XCoordinate = int(pX) # INTEGER 
        self.__YCoordinate = int(pY) # INTEGER

    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self, XChange, YChange):
        self.__XCoordinate = self.__XCoordinate + int(XChange)
        self.__YCoordinate = self.__YCoordinate + int(YChange)

    
CharArr = [] # ARRAY[0 : 9] OF Character

File = open("9618_w22_qp_42 OOP Q2 Only\Characters.txt",'r') # STRING
tempChar = File.readline().strip() # STRING
while tempChar != "": 
    tempX = File.readline().strip() # STRING
    tempY = File.readline().strip() # STRING
    CharArr.append(Character(tempChar, tempX, tempY))
    tempChar = File.readline().strip()

File.close()


Found = False # BOOLEAN
while Found == False:
    chrName = str(input("Please enter a character name : ")) # STRING
    for i in range(len(CharArr)): # INTEGER
        if str(CharArr[i].GetName()).upper() == chrName.upper():
            tempIndex = i
            Found = True


valid = False # BOOLEAN
while valid == False:

    directionInput = str(input("Please enter a character [W][A][S][D]:")) # CHARACTER

    if directionInput == 'A': 
        CharArr[tempIndex].ChangePosition("-1", "0")
        valid = True
    elif directionInput == 'W':
        CharArr[tempIndex].ChangePosition("0", "1")
        valid = True
    elif directionInput == 'S':
        CharArr[tempIndex].ChangePosition("0", "-1")
        valid = True
    elif directionInput == 'D':
        CharArr[tempIndex].ChangePosition("1", "0")
        valid = True
    else:
        valid = False


print(f"{CharArr[tempIndex].GetName()} has changed coordinates to X = {CharArr[tempIndex].GetX()} and Y  = {CharArr[tempIndex].GetY()}")
