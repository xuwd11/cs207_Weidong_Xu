
from enum import Enum
class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    
class BankAccount:
    
    def __init__(self, owner, accountType):
        if not accountType in AccountType:
            raise TypeError('Please enter a valid account type.')
        self.owner = owner
        self.accountType = accountType
        self.balance = 0
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient fund.')
        elif amount < 0:
            raise ValueError('Invalid input.')
        else:
            self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Invalid input.')
        else:
            self.balance += amount
        return self.balance
    
    def __str__(self):
        return 'Account owner: {}, type of account: {}.'.format(self.owner, self.accountType.name)
        
    def __len__(self):
        return self.balance
    
class BankUser:
    
    def __init__(self, owner):
        self.owner = owner
        self.accounts = dict()
    
    def addAccount(self, accountType):
        if not accountType in AccountType:
            raise TypeError('Please enter a valid account type.')
        if accountType in self.accounts:
            raise ValueError('You are allowed to own only one savings/checking account.')
        self.accounts[accountType] = BankAccount(self.owner, accountType)
        
    def getBalance(self, accountType):
        if not accountType in self.accounts:
            raise ValueError('You don\'t have the account.')
        return len(self.accounts[accountType])
    
    def deposit(self, accountType, amount):
        if not accountType in self.accounts:
            raise ValueError('You don\'t have the account.')
        self.accounts[accountType].deposit(amount)
        return len(self.accounts[accountType])
    
    def withdraw(self, accountType, amount):
        if not accountType in self.accounts:
            raise ValueError('You don\'t have the account.')
        self.accounts[accountType].withdraw(amount)
        return len(self.accounts[accountType])
    
    def __str__(self):
        return '{} has {} account(s).\n'.format(self.owner, len(self.accounts)) \
    + '\n'.join(['{} account: balance {}.'.format(name, balance) \
                 for name, balance in sorted([(a.name, len(c)) for a, c in self.accounts.items()])])
    
def ATMSession(bankUser):
    def Interface():
        nonlocal bankUser
        while(True):
            print('Enter Option:\n1)Exit\n2)Create Account\n3)Check Balance\n4)Deposit\n5)Withdraw')
            option = input()
            try:
                option = int(option.strip())
                if option < 0 or option > 5:
                    raise ValueError
            except:
                print('Please enter a valid integer number (from 1 to 5).\n')
                continue
            if 1 == option:
                break
            else:
                print('Enter Option:\n1)Checking\n2)Savings')
                option_type = input()
                try:
                    option_type = int(option_type.strip())
                    if not (1 == option_type or 2 == option_type):
                        raise ValueError
                except:
                    print('Invalid input. Please start over.\n')
                    continue
                if 1 == option_type:
                    accountType = AccountType.CHECKING
                else:
                    accountType = AccountType.SAVINGS
                if 2 == option:
                    try:
                        bankUser.addAccount(accountType)
                        print('{} account has been created successfully.\n'.format(accountType.name))
                        continue
                    except:
                        print('New account setup failed. You\'ve already had a {} account.\n'.format(accountType.name))
                        continue
                else:
                    try:
                        balance = bankUser.getBalance(accountType)
                    except:
                        print('{} account does not exist.\n'.format(accountType.name))
                        continue
                    if 3 == option:
                        print('{} account balance: {}\n'.format(accountType.name, balance))
                        continue
                    else:
                        amount = input('Enter Integer Amount, Cannot Be Negative:')
                        try:
                            amount = int(amount.strip())
                            if amount < 0:
                                raise ValueError
                        except:
                            print('Invalid amount. Please start over.\n')
                            continue
                        if 4 == option:
                            bankUser.deposit(accountType, amount)
                            print('{} has been deposited into {} account. New balance: {}\n'.\
                                  format(amount, accountType.name, bankUser.getBalance(accountType)))
                            continue
                        elif 5 == option:
                            try:
                                bankUser.withdraw(accountType, amount)
                                print('{} has been withdrawn from {} account. New balance: {}\n'.\
                                      format(amount, accountType.name, bankUser.getBalance(accountType)))
                                continue
                            except:
                                print('Insufficient fund.\n')
                                continue
    return Interface