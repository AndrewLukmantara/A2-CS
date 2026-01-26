class Card():

    def __init__(self, pNumber, pColour):
         self.__Number = pNumber # TYPE INTEGER
         self.__Colour = pColour # TYPE STRING

    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    

CardArr = [] # ARRAY OF TYPE Card WITH 30 ELEMENTS
File = open("9618_s22_qp_42/CardValues.txt", 'r')
tempNumber = File.readline().strip() # TYPE INTEGER
while tempNumber != "":
    tempColour = File.readline().strip() # TYPE STRING
    CardArr.append(Card(tempNumber, tempColour))
    tempNumber = File.readline().strip() 

File.close()

selectedCards = [] # ARRAY OF TYPE Card WITH 20 ELEMENTS 

def ChooseCard():

    valid = False # TYPE BOOLEAN

    while valid == False:
        index = int(input("Please enter a number from 1 to 30 : ")) # TYPE INTEGER
        if index < 1 or index > 30:
            print("Invalid number!")
            valid = False

        else:

            index = index - 1 
            chosenCard = CardArr[index] # TYPE Card
            
            alreadyChosen = False # TYPE BOOLEAN

            for i in selectedCards: # i OF TYPE INTEGER
                if i.GetNumber() == chosenCard.GetNumber() and i.GetColour() == chosenCard.GetColour():
                    alreadyChosen = True

            if alreadyChosen == True:
                print("Card already chosen!")
                valid = False
            else:
                print("Card is available!")
                valid = True

    selectedCards.append(chosenCard)
    return index
                            
    

Player1 = [] # ARRAY OF TYPE Card WITH 4 ELEMENTS
Player1.append(CardArr[ChooseCard()])
Player1.append(CardArr[ChooseCard()])
Player1.append(CardArr[ChooseCard()])
Player1.append(CardArr[ChooseCard()])

for i in range(len(Player1)):
    print(f"Number : {Player1[i].GetNumber()}")
    print(f"Colour : {Player1[i].GetColour()}")
