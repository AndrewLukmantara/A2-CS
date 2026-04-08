class Person():
    
    def __init__(self, firstName : str, lastName : str, residence : str):
        self.firstName = firstName
        self.lastName = lastName
        self.residence = residence

    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName
    
    def get_residence(self):
        return self.residence
    
    def set_firstName(self, newfirstName):
        self.firstName = newfirstName

    def set_lastName(self, newlastName):
        self.lastName = newlastName
    
    def print_details(self):
        print(f"First Name : {self.firstName}\nLast Name : {self.lastName}\nResidence : {self.residence}")


class Student(Person):
    
    def __init__(self, firstName : str, lastName : str, residence : str, studentID : str, grade : int):
        super().__init__(firstName, lastName, residence)
        self.studentID = studentID
        self.grade = grade


    def get_studentID(self):
        return self.studentID
    
    def get_grade(self):
        return self.grade

    def set_studentID(self, newstudentID):  
        self.studentID = newstudentID

    def set_grade(self, newGrade):
        self.grade = newGrade


    def print_details(self):
        print(f"First Name : {self.firstName}\nLast Name : {self.lastName}\nResidence : {self.residence}\nStudentID = {self.studentID}\nGrade = {self.grade}")
    
    
class Worker(Person):
    
    def __init__(self, firstName : str, lastName : str, residence : str, ID : str, salary : int):
        super().__init__(firstName, lastName, residence)
        self.ID = ID
        self.salary = salary


    def get_ID(self):
        return self.ID
    
    def get_salary(self):
        return self.salary

    def set_ID(self, newID):  
        self.ID = newID

    def set_salary(self, newSalary):
        self.salary = newSalary


    def print_details(self):
        print(f"First Name : {self.firstName}\nLast Name : {self.lastName}\nResidence : {self.residence}\nID = {self.ID}\nSalary = {self.salary}")


personArr = []

personFile = open("C:/Users/62818/OneDrive/A Level CS/A2_Algorithm_Revision/person.txt", "r")
line = personFile.readline().strip()
while line != "":
    store = line.split(",")
    if store[0] == "Student":
        personArr.append(Student(store[1], store[2], store[3], store[4], int(store[5])))
    elif store[0] == "Worker":
        personArr.append(Worker(store[1], store[2], store[3], store[4], int(store[5])))

    line = personFile.readline().strip()


personFile.close()


for i in range(len(personArr)):
    personArr[i].print_details()