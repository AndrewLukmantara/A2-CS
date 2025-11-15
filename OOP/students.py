class Student():

    def __init__(self, studentName, studentAge, studentGender):

        # public attributes

        # self.name = studentName
        # self.age = studentAge
        # self.gender = studentGender

        # protected attributes

        # self._name = studentName
        # self._age = studentAge
        # self._gender = studentGender

        # private attributes

        self.__name = studentName
        self.__age = studentAge
        self.__gender = studentGender


    def display_info(self):
        print(f"Name : {self.__name}\nAge : {self.__age}\nGender {self.__gender}\n")

    def return_info(self):
        return (f"Name : {self.__name}\nAge : {self.__age}\nGender {self.__gender}\n")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_name(self, newName):
        self.__name = newName
    
    # def __str__(self):
        # return (f"Name : {self.name}\nAge : {self.age}\nGender {self.gender}\n")

    

# print(student1.display_info()) will include "None" in the output

student1 = Student("Andrew", 18, "male")
student1.display_info()
print(student1) # if there is no __str__, it shows the memory where it is created
print(student1.return_info())

student2 = Student("Bobby", 20, "male")
print(student2)

studentsArr = []
studentsArr.append(student1)
studentsArr.append(student2)


# same thing here. If there is no __str__, it will show the memory locations
for i in studentsArr:
    print(i)



# print(student1.name) 
# this must never be possible as attributes must be private / accessible only from within the class. To prevent this, we use access modifiers


# The three access modifers
# 1. Public - Attributes can be accessible from outside the class
# 2. Private - Attributes can only be accessible from within the class (__)
# 3. Protected - (_)

# print(student1.__name)
# error as private access modifier is used

# print(student1._name)
# if protected access modifier is used, it will still work. This is because the protected modifier only tells the user to not do it


# Principles of OOP
# 1. All attributes are set to private
# 2. All methods are set to public'

# All OOPs usually have 2 methods
# 1. Getter methods
# 2. Setter methods

print(student1.get_name())
student1.set_name("Khan")
print(student1.get_name())

print(student1.get_gender())