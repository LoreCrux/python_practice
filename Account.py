class Account:
    """A class that does a simple withdraw and deposit to an account"""
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount_dpt):
        self.balance = self.balance + amount_dpt
        print(f'Amount deposited: {self.balance}')
        
    def withdraw(self, amount_wdw):
        self.balance = self.balance - amount_wdw
        print(f'Amount withdrawn: {self.balance}')
        if amount_wdw > self.balance:
            return f'Account overdrawn, New Account Balance: {self.balance}'
        return self.balance

# Instantiate the class
acct1 = Account('Jose',100)

# Show the account owner attribute
acct1.owner

# Show the account balance attribute
acct1.balance

# Make a series of deposits and withdrawals
acct1.deposit(50)

# Withdraw from account
acct1.withdraw(75)

# Make a withdrawal that exceeds the available balance
acct1.withdraw(150)