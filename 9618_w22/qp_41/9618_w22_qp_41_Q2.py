class Card():
    def __init__(self, pNumber, pColour):
        self.__Number = pNumber # INTEGER
        self.__Colour = pColour # STRING
        self.__size = 20
     
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
    def GetSize(self):
        return self.__size
    
randomCard = Card(10, "Purple")
print(randomCard.GetSize())

    
class Hand():
    def __init__(self, pFirstCard, pSecondCard, pThirdCard, pFourthCard, pFifthCard):
        self.__FirstCard = 0 # INTEGER 
        self.__NumberCards = 5 # INTEGER
        self.__Cards = [pFirstCard, pSecondCard, pThirdCard, pFourthCard, pFifthCard] # ARRAY[0:9] OF Card 

    def GetCard(self, index):
        return self.__Cards[index]
    


r1 = Card(1, "red")
r2 = Card(2, "red")
r3 = Card(3, "red")
r4 = Card(4, "red")
r5 = Card(5, "red")

b1 = Card(1, "blue")
b2 = Card(2, "blue")
b3 = Card(3, "blue")
b4 = Card(4, "blue")
b5 = Card(5, "blue")

y1 = Card(1, "yellow")
y2 = Card(2, "yellow")
y3 = Card(3, "yellow")
y4 = Card(4, "yellow")
y5 = Card(5, "yellow")

p1 = Hand(r1, r2, r3, r4, y1)
p2 = Hand(y2, y3, y4, y5, b1)

def CalculateValue(pHand):
    score = 0 # INTEGER
    for i in range(5): # i : INTEGER
        if pHand.GetCard(i).GetColour() == "red":
            score = score + 5
        elif pHand.GetCard(i).GetColour() == "blue":
            score = score + 10
        elif pHand.GetCard(i).GetColour() == "yellow":
            score = score + 15

    return score

if CalculateValue(p1) > CalculateValue(p2):
    print("Player 1 has more points than Player 2! Player 1 Wins!")
elif CalculateValue(p2) > CalculateValue(p1):
    print("Player 2 has more points than Player 1! Player 2 Wins!")
else:
    print("A Draw!")