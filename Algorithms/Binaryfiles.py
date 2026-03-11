# Open the file for reading / writing in binary
# Import a library called pickle

import pickle
class Student:
    def __init__(self, Name, ID):
        self.Name = Name
        self.ID = ID

student1 = Student("Albert", "123")
file = open("C:/Users/AndrewCL JC2Hope/OneDrive/A Level CS/Algorithms/Students.txt", "wb")

pickle.dump(student1, file) # Storing the record

file.close()

file = open("C:/Users/AndrewCL JC2Hope/OneDrive/A Level CS/Algorithms/Students.txt", "rb")

tempStudent = pickle.load(file)
print(tempStudent.Name)
print(tempStudent.ID)