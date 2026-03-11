WordArray = []
Numberwords = 0


def Play():
    
    global WordArray, Numberwords
    
    print(f"Main word : {WordArray[0]}") 
    print(f"Number of answers : {len(WordArray) - 1}")
    Stop = False
    correct = 0
    while not Stop:

        user = str(input("Please enter a word! Enter 'no' to stop : "))

        if user == "no":
            Stop = True
            Percentage = (correct / (len(WordArray) - 1)) * 100
            print(f"{Percentage}% Correct")
            print("You did not enter : ")
            for i in range(1, len(WordArray)):
                if WordArray[i] != -1:
                    print(WordArray[i])

        elif user in WordArray:
            print("It is an answer!")
            correct += 1
            for i in range(1, len(WordArray)):
                if WordArray[i] == user:
                    WordArray[i] = -1
                    break
        
        else:
            print("It is not an answer!")



def ReadWords(filename : str):

    global WordArray, Numberwords

    file = open(filename, "r")
    WordArray.append(file.readline().strip())
    line = file.readline().strip()
    ans = 1
    while line != "":
        WordArray.append(line)
        ans += 1
        line = file.readline().strip()
    
    Numberwords = ans

    Play()


level = str(input("Please enter the level difficulty [easy][medium][hard]: "))
if level == "easy":
    ReadWords(f"9618_s24\Easy.txt")
elif level == "medium":
    ReadWords(f"9618_s24\Medium.txt")
elif level == "hard":
    ReadWords(f"9618_s24\Hard.txt")