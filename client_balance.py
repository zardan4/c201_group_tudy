class Client:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = float(balance)
        self.session = None

    def minus_money(self, amount: float):
        if amount < 0:
            return False

        if self.balance >= amount:
            self.balance -= amount
            return True

        return False

    def add_balance(self, amount: float):
        if amount > 0:
            self.balance += amount
            return True

        return False

    def get_balance(self):
        return self.balance


User = Client