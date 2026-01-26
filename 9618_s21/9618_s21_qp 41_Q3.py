class TreasureChest():

    # Initializing

    def __init__(self, question, answer, points):

        self.__question = question # Private attribute of Type String
        self.__answer = answer # Private attribute of Type Integer
        self.__points = points # Ptrivate attribute of Type Integer
    
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, userAnswer):
        if userAnswer == self.__answer:
            return True
        else:
            return False
        
    def getPoints(self, userAttempts):
        if userAttempts == 1:
            return self.__points
        elif userAttempts == 2:
            return int(self.__points / 2)
        elif userAttempts == 3 or userAttempts == 4: 
            return int(self.__points / 4)
        else:
            return 0
        


def readData():

    try: 

        # DECLARE file, line : STRING
        # DECLARE arrayTreasure : ARRAY[0 : 4] OF TreasureChest
        # DECLARE tempQuestiom, tempAnswer, tempPoints : STRING

        file = open("TreasureChestData.txt", 'r')
        global arrayTreasure
        arrayTreasure = [] 


        line = file.readline().strip()
        while line != "":

            tempQuestion = line 
            tempAnswer = file.readline().strip()
            tempPoints = file.readline().strip()
            arrayTreasure.append(TreasureChest(tempQuestion, int(tempAnswer), int(tempPoints)))
            line = file.readline().strip() 

    except FileNotFoundError:
        print("File not found!")
    

readData()
UQuestionNum = int(input("Enter a question number from 1 to 5 : "))

# DECLARE i : INTEGER
# DECALRE Count : INTEGER
# DECLARE UAnswer : INTEGER

for i in range(5):
    if i == UQuestionNum - 1:
        print(arrayTreasure[i].getQuestion())
        UAnswer = int(input("Enter the answer : "))
        Count = 1
        while arrayTreasure[i].checkAnswer(UAnswer) == False:
            print("Incorrect!")
            UAnswer = int(input("Enter the answer : "))
            Count = Count + 1
        print("Correct!")
        print(f"{arrayTreasure[i].getPoints(Count)} points awarded!")
        break



