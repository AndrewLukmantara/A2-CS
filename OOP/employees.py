class Employee:
    def __init__(self, Ename, Bpay, EGender, Ehours, OTHours, Allowance):
        self.name = Ename
        self.BasicPay = Bpay
        self.gender = EGender
        self.hours = Ehours
        self.othours = OTHours
        self.allowance = Allowance
    
    def salary(self):
        return self.hours * self.allowance + 500 * self.othours

    def show_detail(self):
        print(f"{self.name} is a {self.gender}")


employee1 = Employee("Nonk", "Male", 5, 2, 500)
employee1.show_detail()
print(f"Employee salary is {employee1.salary()}")