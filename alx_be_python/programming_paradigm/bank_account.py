class BankAccount:
    def __init__(self, balance=0):
        self.account_balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
