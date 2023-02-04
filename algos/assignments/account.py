class Account:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            print('You have insufficient balance')
            return
        self.balance -= amount
        print(f'We just removed ${amount} to you account. Total balance now: ${self.balance}')

    def deposit(self, amount: float):
        self.balance += amount
        print(f'We just added ${amount} to you account. Total balance now: ${self.balance}')

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    account = Account('Justo', 89)
    print(account)
    print(account.balance)
    print(account.owner)

    account.withdraw(67)
    account.deposit(100)
    account.withdraw(34)
