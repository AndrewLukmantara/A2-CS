# Object Oriented Programming

class Student (): # Encapsulation
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")
        
    


student = Student("John Doe", 16, "S12345")
student.display_info()



# In Pseudocode
# TYPE Student

    # DECLARE Name : STRING
    # DECLARE Age : INTEGER
    # DECLARE Student_ID : STRING
    
# ENDTYPE

# DECLARE Student1 : Student
# Student1.Name <- "Andrew"
# Student1.Age <- "17"
# Student1.Student_ID <- "S67890"


class Teacher(): # Encapsulation
    
    def __init__(self, name, age, teacher_id):
        self.name = name
        self.age = age
        self.teacher_id = teacher_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Teacher ID: {self.teacher_id}")




teacher = Teacher("John Doe", 40, "T1923")
teacher.display_info()
