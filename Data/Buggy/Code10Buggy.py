# # Buggy Code
# 
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
# 
#     def deposit(self, amount):
#         if amount < 0:
#             self.balance += amount
#             return f"${amount} deposited. New balance: ${self.balance}"
#         return "Deposit amount must be positive."
# 
#     def withdraw(self, amount):
#         if amount > self.balance:
#             return "Insufficient funds."
#         elif amount > 0:
#             self.balance -= amount
#             return f"${amount} withdrawn. Remaining balance: ${self.balance}"
#         return "Withdrawal amount must be positive."
# 
#     def check_balance(self):
#         return f"Account owner: {self.owner}, Balance: ${self.balance}"
# 

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited. New balance: ${self.balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount > 0:
            self.balance -= amount
            return f"${amount} withdrawn. Remaining balance: ${self.balance}"
        return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Account owner: {self.owner}, Balance: ${self.balance}"