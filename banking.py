from random import randint

class SavingsAccount():

    def __init__(self):
        self.savingAccounts = {}

    def createAccount(self,name,deposit):
        self.accountNumber = randint(10000,99999)
        self.savingAccounts[self.accountNumber] = [name,deposit]
        print("Your account number is {}".format(self.accountNumber))

    def authenticate(self,name,accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name:
                print("Authentication Successful")
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self,withdrawAmount):
        if withdrawAmount <= self.savingAccounts[self.accountNumber][1]:
            self.savingAccounts[self.accountNumber][1] -= withdrawAmount
            self.displayBalance()

    def deposit(self,depo):
        self.savingAccounts[self.accountNumber][1] += depo
        self.displayBalance()

    def displayBalance(self):
        print("Print Available Balance : {}".format(self.savingAccounts[self.accountNumber][1]))




savings =  SavingsAccount()
while True:
    print("Enter 1 to create a new Account")
    print('Enter 2 to open an existing Account')
    print("Enter 3 to exit from using the service")

    userChoice = int(input())
    if userChoice is 1:
        print("Enter the name of the user :")
        name = input()
        print("Enter the initial deposit :")
        deposit = int(input())
        savings.createAccount(name, deposit)
    elif userChoice is 2:
        print("Enter the name of the user")
        name = input()
        print("Enter your account number")
        accountNumber = int(input())
        authenticationStatus = savings.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to show Available Balance")
                print("Enter 4 to be back to previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    withdrawAmount = int(input())
                    savings.withdraw(withdrawAmount)
                elif userChoice is 2:
                    depo = int(input())
                    savings.deposit(depo)
                elif userChoice is 3:
                    savings.displayBalance()
                else:
                    break
    elif userChoice is 3:
        quit()
















