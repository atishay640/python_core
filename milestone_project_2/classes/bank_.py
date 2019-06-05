'''
A Card from the deck

'''

class Bank:
    def __init__(self, balance = 0,user = 'Player' ):
        self.balance = balance
        self.user = user

    def debit(self,amount):
        if amount > self.balance:
            raise ValueError
        self.balance = self.balance - amount
        return self.balance

    def credit(self,amount):
        self.balance = self.balance + amount
        return self.balance






