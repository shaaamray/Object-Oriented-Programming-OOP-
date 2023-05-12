class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

    def get_accountNumber(self):
        return self.__account_number

# create a instance now


account = BankAccount("12233454645", 5000)



account.deposit(500)
account.withdraw(200)

print(account.get_balance())
print(account.__account_number)  # will give an Attribute error
