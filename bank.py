import csv
import os

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit value must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("deposit value must be positive")
        if amount > self.balance:
            raise ValueError("insufficient amount")
        self.balance -= amount

    def transfer(self, target_account, amount):
        self.withdraw(amount)
        target_account.deposit(amount)

    def to_row(self):
        return [self.name, "%.2f" % self.balance]

    @staticmethod
    def from_row(row):
        return Account(row[0], float(row[1]))


class Bank:
    def __init__(self, data_file="data.csv"):
        self.data_file = data_file
        self.accounts = {}
        self.load()

    def create_account(self, name, balance):
        if name in self.accounts:
            raise ValueError("account already existed")
        self.accounts[name] = Account(name, balance)
        self.save()

    def deposit(self, name, amount):
        self.get_account(name).deposit(amount)
        self.save()

    def withdraw(self, name, amount):
        self.get_account(name).withdraw(amount)
        self.save()

    def transfer(self, from_name, to_name, amount):
        if from_name == to_name:
            raise ValueError("cannot transfer to yourself")
        from_account = self.get_account(from_name)
        to_account = self.get_account(to_name)
        from_account.transfer(to_account, amount)
        self.save()

    def get_account(self, name):
        if name not in self.accounts:
            raise ValueError("account does not exist")
        return self.accounts[name]

    def save(self):
        with open(self.data_file, "w") as f:
            writer = csv.writer(f)
            for account in self.accounts.values():
                writer.writerow(account.to_row())

    def load(self):
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                acc = Account.from_row(row)
                self.accounts[acc.name] = acc
