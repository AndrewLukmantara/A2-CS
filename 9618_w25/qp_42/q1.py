class Bird():
    def __init__(self, Species, DistancePerHour):
        self.__Species = Species # String
        self.__DistancePerHour = DistancePerHour # Real
        self.__XPosition = 500.0 # Real
        self.__YPosition = 500.0 # Real

    def GetPosition(self):
        return str(f"X : {self.__XPosition} Y : {self.__YPosition}")
    
    def GetSpecies(self):
        return self.__Species
    
    def Move(self, direction : str, minutes : int):
        
        distance = (self.__DistancePerHour / 60) * minutes

        match direction:

            case 'N':
                self.__YPosition = self.__YPosition + distance

            case 'S':
                self.__YPosition = self.__YPosition - distance

            case 'W':
                self.__XPosition = self.__YPosition - distance

            case 'E':
                self.__XPosition = self.__YPosition + distance


Bird1 = Bird("Cockatiel", 71.0)
Bird2 = Bird("Macaw", 56.0)

print(f"Species : {Bird1.GetSpecies()}]\n{Bird1.GetPosition()}")
print(f"Species : {Bird2.GetSpecies()}]\n{Bird2.GetPosition()}") 

bird_selection = int(input("Please select a bird. [1] for Cockatiel and [2] for Macaw : ")) # INTEGER
direction = str(input("Enter the direction the bird has been travelling : ")) # STRING
time = int(input("Enter the time that the bird has been travelling : ")) # INTEGER


if bird_selection == 1:
    Bird1.Move(direction, time)
    print(Bird1.GetPosition())
elif bird_selection == 2:
    Bird2.Move(direction, time)
    print(Bird2.GetPosition())