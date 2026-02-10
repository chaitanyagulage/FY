class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account: {self.account_number} | Current Balance: ${self.balance}")

# --- Testing the Class ---
print("--- 5. Bank Account Experiment ---")
my_account = BankAccount("ACC-12345", 1000)
my_account.check_balance()
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(5000) # Test insufficient funds
print("-" * 30)
