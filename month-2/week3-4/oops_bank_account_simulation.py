# Bank Account Simulation
# Problem: Create a class BankAccount with methods to:
# deposit(amount)
# withdraw(amount)
# get_balance()
# Ensure that withdrawals do not result in a negative balance.
# Objective: Understand how to implement simple class-based simulations.



class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance 

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    
    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance


my_account = BankAccount(100)  


my_account.deposit(50)


my_account.withdraw(30)


my_account.withdraw(150)


my_account.get_balance()
