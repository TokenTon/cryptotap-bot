# TON Wallet Storage

class Wallet:
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
        self.balance = 0  # Initialize balance to 0

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Amount must be positive")

    def subtract_balance(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f'Wallet({self.wallet_address}): {self.balance} TON'