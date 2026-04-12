class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance!")

    def check_balance(self):
        print(f"Current Balance: {self.balance}")


# Example Usage
acc = BankAccount(101, 5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()