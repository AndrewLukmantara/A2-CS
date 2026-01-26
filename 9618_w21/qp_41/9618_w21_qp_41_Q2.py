class Picture():

    def __init__(self, PDescription, PWidth, PHeight, PFrameColour):

        # Description : STRING
        # Width : INTEGER
        # Height : INTEGER
        # FrameColour : STRING

        self.__Description = PDescription
        self.__Width = PWidth
        self.__Height = PHeight
        self.__FrameColour = PFrameColour
    
    # Getter Methods

    def GetDescription(self):
        return self.__Description
    
    def GetWidth(self):
        return self.__Width
    
    def GetHeight(self):    
        return self.__Height
    
    def GetFrameColour(self):
        return self.__FrameColour
    
    def SetDescription(self, newDescription): # newDescription : STRING
        self.__Description = newDescription 



# ArrPic : ARRAY[0 : 99] OF Picture
ArrPict = [None] * 100 


def ReadData():
    try:

        # count : INTEGER
        # line1, line2, line3, line4 : STRING

        count = 0
        file = open("Pictures.txt",'r')
        line1 = file.readline().strip()
        while line1 != "":
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            line4 = file.readline().strip()
            ArrPict[count] = Picture(line1, int(line2), int(line3), line4)
            count = count + 1
            line1 = file.readline().strip()
        
        return count

    except FileNotFoundError:
        print("File Not Found!")

ReadData()

# length : INTEGER
# userColour : STRING
# maxHeight : INTEGER
# maxWidth : INTEGER

length = ReadData()
userColour = str(input("Please enter a colour :")).lower()
maxHeight = int(input("Please enter the maximum height :"))
maxWidth = int(input("Please enter the maximum width :"))

for i in range(0, length):
    if ArrPict[i].GetFrameColour() == userColour and ArrPict[i].GetHeight() <= maxHeight and ArrPict[i].GetWidth() <= maxWidth:
        print(f"Description : {ArrPict[i].GetDescription()}")
        print(f"Height : {ArrPict[i].GetHeight()}")
        print(f"Width : {ArrPict[i].GetWidth()}")

