import random


class Account:
    def __init__(self):
        self.number = random.randint(100_000_000_000_000_000_000, 999_999_999_999_999_999_999)
        self.balance = 0.0

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawn", amount)

    def add_money(self, amount):
        if amount > 0:
            self.balance += amount
            print("Added", amount)


class Client:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)

    def get_total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def add_client(self, client):
        if isinstance(client, Client):
            self.clients.append(client)

    def get_total_deposits(self):
        total = 0
        for client in self.clients:
            total += client.get_total_balance()
        return total


# programmas testa izpilde

banka = Bank(name="Jaunā banka")

aldis = Client(name="Aldis")
zane = Client(name="Zane")

banka.add_client(aldis)
banka.add_client(zane)

account_1 = Account()
print(account_1.number)
aldis.add_account(account=account_1)

account_1.add_money(500)
account_1.withdraw(20)
print(account_1.balance)

account_2 = Account()
aldis.add_account(account=account_2)
account_2.add_money(20)

account_3 = Account()
zane.add_account(account=account_3)
account_3.add_money(500)

print(banka.name, "has totally", banka.get_total_deposits())
