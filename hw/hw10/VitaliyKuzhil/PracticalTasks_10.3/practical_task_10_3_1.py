class BankAccount:

    def __init__(self, account_number: str, account_holder: str, balance: float):
        '''
        Init artributes: 
        
        account_number (string)
        account_holder (string)
        balance (float)
        '''
        self.__dict__['_account_number'] = account_number
        self.__dict__['account_holder'] = account_holder
        self.__dict__['_balance'] = balance


    def __getattribute__(self, name):
        '''
        Redefining the __getattribute__ dunder method
        '''
        try:
            return super().__getattribute__(name)
        except AttributeError:
            raise AttributeError


    def __setattr__(self, name, value):
        '''
        Redefining the __setattr__ dunder method
        '''
        if name == 'account_holder':
            raise AttributeError
        super().__setattr__(name, value)


    @staticmethod
    def check_num(amount:int|float):
        '''
        Method that checking amount > 0 
        '''
        return float(amount) > 0   


    def deposit(self, amount:int|float):
        '''
        Method that allows the account holder to deposit money into the account
        '''
        if BankAccount.check_num(amount):
            self._balance += amount


    def withdraw(self, amount:int|float):
        '''
        Method that allows the account holder to withdraw money from the account;
        write "Insufficient funds" if money doesn't enough
        '''
        if BankAccount.check_num(amount):
            
            if self._balance < amount:
                print('Insufficient funds')
            else:
                self._balance -= amount


    def check_balance(self):
        '''
        Method that returns the current balance of the account
        '''
        return self._balance
