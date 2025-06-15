"""
Understand the fundamentals of OOP in Python by implementing a 
BankAccount class that encapsulates banking operations.
"""
class BankAccount:
    def __init__(self, current_balance):
        self._current_balance = float(current_balance)
    def deposit(self, amount):
        if amount >= 0:
            self._current_balance += amount
        else:
            pass
    def withdraw(self, amount):
        if self._current_balance >= amount and amount > 0:
            self._current_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self._current_balance:.2f}")