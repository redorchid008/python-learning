# bank.py
from abc import ABC, abstractmethod

# -----------------------------
# Abstraction (Abstract Class)
# -----------------------------
class Account(ABC):
    def __init__(self, account_holder, balance=0):
        # Encapsulation: protected attributes
        self._account_holder = account_holder
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method: Must be implemented by child classes."""
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ₹{amount}. New balance: ₹{self._balance}"
        return "Deposit amount must be positive!"

    def get_balance(self):
        return self._balance

    def get_account_holder(self):
        return self._account_holder


# -----------------------------
# Inheritance + Polymorphism
# -----------------------------
class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return f"SavingsAccount: Withdrew ₹{amount}. New balance: ₹{self._balance}"
        return "SavingsAccount: Insufficient funds!"

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Interest of ₹{interest:.2f} added. New balance: ₹{self._balance}"


class CurrentAccount(Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=5000):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
            return f"CurrentAccount: Withdrew ₹{amount}. New balance: ₹{self._balance}"
        return "CurrentAccount: Overdraft limit exceeded!"


# -----------------------------
# Example usage (optional for running directly)
# -----------------------------
if __name__ == "__main__":
    savings = SavingsAccount("Avijit", 10000)
    current = CurrentAccount("Chatterjee", 5000)

    print(savings.deposit(2000))
    print(savings.withdraw(2500))
    print(savings.add_interest())

    print(current.deposit(3000))
    print(current.withdraw(9000))

    print(f"{savings.get_account_holder()} Balance: ₹{savings.get_balance()}")
    print(f"{current.get_account_holder()} Balance: ₹{current.get_balance()}")
