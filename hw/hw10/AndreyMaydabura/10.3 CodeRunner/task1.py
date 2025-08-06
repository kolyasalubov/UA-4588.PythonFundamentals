class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__balance = balance
        self.__account_holder = account_holder

    @property
    def account_holder(self):
        return self.__account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance
