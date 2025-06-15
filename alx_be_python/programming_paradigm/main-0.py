import sys
from bank_account import BankAccount

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main-0.py deposit|withdraw amount")
        sys.exit(1)

    action = sys.argv[1]
    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("Amount must be a number")
        sys.exit(1)

    account = BankAccount()

    if action == "deposit":
        account.deposit(amount)
    elif action == "withdraw":
        account.withdraw(amount)
    else:
        print("Invalid action. Use 'deposit' or 'withdraw'")
        sys.exit(1)

    print(account.get_balance())

