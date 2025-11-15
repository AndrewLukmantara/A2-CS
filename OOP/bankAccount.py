class BankAccount():
    def __init__(self, accNum, bal):
        self.__accountNumber = accNum
        self.__balance = bal

    def get_accountNumber(self):
        return self.__accountNumber

    def get_balance(self):
        return self.__balance
    
    def set_accountNumber(self, newAccNum):
        self.__accountNumber = newAccNum

    def set_balance(self, newBalance):
        self.__balance = newBalance

    def deposit(self, dpst):
        if dpst > 0:
            self.__balance = self.__balance + dpst

    def withdraw(self, withdraw):
        if withdraw > 0 and withdraw < self.__balance:
            self.__balance = self.__balance - withdraw

    

accountArray = []
account1 = BankAccount(1111, 2000)
account2 = BankAccount(2222, 3300)
account3 = BankAccount(3333, 400)

account1.set_balance(9000)
print(f"Balance : {account1.get_balance()}")

accountArray.append(account1)
accountArray.append(account2)
accountArray.append(account3)

for acc in accountArray:
    deposit = int(input("Please enter how much you want to deposit"))
    acc.deposit(deposit)
    withdrawal = int(input("Please enter how much you want to withdraw"))
    acc.withdraw(withdrawal)
    print(f"Balance : {acc.get_balance()}")