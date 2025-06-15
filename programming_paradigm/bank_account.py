"""
Understand the fundamentals of OOP in Python by implementing a 
BankAccount class that encapsulates banking operations.
"""
class BankAccount:
    def __init__(self, current_balance):
        self.current_balance = current_balance
    def deposit(self, amount):
        if amount >= 0:
            self.current_balance += amount
        else:
            pass
    def withdraw(self, amount):
        if self.current_balance >= amount and amount > 0:
            self.current_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.current_balance}")