class Employee():
        
    # Initiliazing of attributes
    
    def __init__(self, pempID, pempName, psalary):
        self.__empID = pempID  # type string
        self.__empName = pempName # type string
        self.__salary = psalary # type real
    
    # Getters
    
    def get_empID(self):
        return self.__empID
    
    def get_empName(self):
        return self.__empName
    
    def get_salary(self):
        return self.__salary
    
    # Setters
    
    def set_empID(self, newempID):
        self.__empID = newempID
    
    def set_empName(self, newempName):
        self.__empName = newempName
        
    def set_salary(self, newSalary):
        self.__salary = newSalary
    
    # Showing employee details

    def showDetails(self):
        print(f"Name : {self.__empName}\nID : {self.__empID}\nSalary : {self.__salary}")
        
    # Increasing the salary by percentage
    
    def increaseSalary(self, percentage):
        self.__salary = self.__salary + self.__salary * percentage/100
        

# Creating 4 Employee Objects

Employee1 = Employee("0001", "John", 9702.50)
Employee2 = Employee("0002", "Alice", 8500.00)
Employee3 = Employee("0003", "Michael", 10250.75)
Employee4 = Employee("0004", "Sofia", 9200.30)

# Creating an empty array

empArr = []

# Initializing the array with the Employee objects

empArr.append(Employee1)
empArr.append(Employee2)
empArr.append(Employee3)
empArr.append(Employee4)

# Increasing the salaries and showing the details

for emp in empArr:
    emp.showDetails()
    pIncrease = float(input(f"PLease enter the percentage increase for {emp.get_empName()}"))
    emp.increaseSalary(pIncrease)
    emp.showDetails()
    