# Create an account
# perform operations like add money, withdraw money


class Account:

    def __init__(self,balance,acc_holder):
        self.balance = balance
        self.holder = acc_holder


    def deposite(self,amount):
        if amount > 0:
            self.balance += amount
            print("{} rupees credited to your account.".format(amount))
            print("Updated balace : {}".format(self.balance))
        else:
            print("Amount can not be zero or negative")


    def withdraw(self,amount):
        if amount > 0:
            self.balance -= amount
            print("{} rupees debited from your account.".format(amount))
            print("Updated balace : {}".format(self.balance))
        else:
            print("Amount can not be zero or negative")

    def __str__(self):
        print('Account holder : {}'.format(self.holder))
        print('Balance : {}'.format(self.balance))
        return ''


my_account = Account(balance= 500,acc_holder="Atishay Sharma")
print('-----')
print(my_account)
print('-----')
my_account.deposite(amount=600)
my_account.withdraw(10)
my_account.withdraw(1000)

print('-----')
print(my_account)

