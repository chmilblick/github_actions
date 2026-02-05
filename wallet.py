

class Wallet:
    def __init__(self, balance: float = 0.0):
        self.balance = balance

    def add_cash(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            msg = 'Not enough available to spend {}'.format(amount)
            raise InsufficientAmount(msg)
        self.balance -= amount

    def spend_cash(self, amount: float):
        self.withdraw(amount)


class InsufficientAmount(Exception):
    pass
