# encapsulation meaning Hide details
# 3 types of access modifier - public, private, protected
class BankAccount:
    def __init__(self, account_holder, balance):
        self._account_holder = account_holder
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
            print(f"Balance set to ${self._balance}")
        else:
            print("Invalid balance.")

# Create a BankAccount instance
account = BankAccount("Alice", 1000)

# Accessing attributes directly (not recommended)
print(account._account_holder)  # Output: Alice

# Accessing attributes through methods (encapsulation)
print(account.get_balance())    # Output: 1000

# Depositing and withdrawing
account.deposit(500)            # Output: Deposited $500. New balance: $1500
account.withdraw(200)           # Output: Withdrew $200. New balance: $1300

# Trying to set negative balance (encapsulation)
account.set_balance(-200)       # Output: Invalid balance.

# Trying to withdraw more than balance (encapsulation)
account.withdraw(1500)          # Output: Insufficient funds or invalid withdrawal amount.

"""In this code, we have defined a 'BankAccount' class that demonstrates encapsulation:

The '_account_holder' and '_balance' attributes are designated as "protected" by convention using a single underscore. This indicates that these attributes are intended to be accessed only within the class or subclasses.

Private Attributes: By convention, attributes that should not be directly accessed from outside the class are marked as private using a double underscore (__). For example, 'self.__balance'.
"""