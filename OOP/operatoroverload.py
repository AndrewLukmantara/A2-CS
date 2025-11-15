class Student():

    def __init__(self, Pgrade1, Pgrade2):
        self.grade1 = Pgrade1
        self.grade2 = Pgrade2

    def get_grade1(self):
        return self.grade1
    
    def get_grade2(self):
        return self.grade2

    def __add__(self, other):
        return self.grade1 + other.grade1 + self.grade2 + other.grade2


s1 = Student(30, 40)
s2 = Student(40, 50)
print(s1 + s2)