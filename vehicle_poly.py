#Bank Account
class BankAccount:
    def __init__(self, account_no, balance=0.00):
        self.account_no = account_no
        self.balance = balance
    def deposit(self, amount):
        if amount >=0:
            self.balance+=amount
            print(f"Deposited: Rs.{amount}. New balance: Rs.{self.balance}")
        else:
            print("Deposited amount must be positive.")
    def withdrawal(self, amount):
        if amount >0:
            if amount <= self.balance:
                self.balance-=amount
                print(f"Withdrawal: Rs.{amount}.Remaining Balance: Rs.{self.balance}")
            else:
                print("Insufficient Balance.")
        else:
            print("Withdrawal amount must be positive.")
    def check_balance(self):
        print(f"Account No.: {self.account_no}")
        print(f"Current Balance: {self.balance}")
Account=BankAccount("SBI1234", 10000)
Account.deposit(500)
Account.withdrawal(100)
Account.check_balance()