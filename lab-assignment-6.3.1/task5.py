class BankAccount:
    def __init__(self, name, balance=0):
        """
        Initialize the BankAccount with owner's name and starting balance.
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a positive amount to the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a positive amount if sufficient balance exists.
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """
        Print the current balance.
        """
        print(f"Current balance: {self.balance}")

# --- Console interaction ---

# Get user input for account creation
name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))

# Create BankAccount object
account = BankAccount(name, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Exiting. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")

"""
Code Explanation:
- The BankAccount class models a simple bank account with deposit, withdraw, and balance check methods.
- The __init__ method initializes the account with a name and starting balance.
- deposit() adds a positive amount to the balance.
- withdraw() subtracts a positive amount if enough balance is available.
- check_balance() prints the current balance.
- The console interaction lets the user create an account and perform operations in a loop.
"""