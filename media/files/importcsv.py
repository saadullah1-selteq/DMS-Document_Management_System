import csv

class Bank:
    BankName = "Standard Chartered Bank"
    Branch = "Johar Town Lahore"
    filename = 'bank_data.csv'  # CSV file to store account data
    transactions_filename = 'transactions.csv'  # CSV file to store transaction details

    def __init__(self, username, pin, address):
        self.username = username
        self.pin = pin
        self.address = address
        self.balance = 0
        self.load_account_data()

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully")
        self.save_account_data()
        self.save_transaction_data('Deposit', amount)

    def transfer(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} transferred successfully")
            self.save_account_data()
            self.save_transaction_data('Transfer', amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def welcome_message(self):
        print(f"HEY {self.username}, your account is created in our bank successfully")
        print(f"Welcome to {Bank.BankName}, {Bank.Branch}")

    def transaction_menu(self):
        while True:
            print("\nPlease select any option for transaction:")
            print('1. Deposit Amount\n2. Transfer Amount\n3. Check the balance\n4. Stop Transaction')
            option = int(input(''))

            if option == 1:
                amount = float(input("Enter deposited amount: "))
                self.deposit(amount)
            elif option == 2:
                amount = float(input("Enter transfer amount: "))
                self.transfer(amount)
            elif option == 3:
                self.check_balance()
            elif option == 4:
                print("Thanks for the transaction")
                break
            else:
                print("Invalid option, please try again")

    def save_account_data(self):
        with open(Bank.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, self.pin, self.address, self.balance])

    def load_account_data(self):
        try:
            with open(Bank.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == self.username and row[1] == self.pin:
                        self.balance = float(row[3])
                        break
        except FileNotFoundError:
            pass  # No file found, proceed with default values

    def save_transaction_data(self, transaction_type, amount):
        with open(Bank.transactions_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, transaction_type, amount, self.balance])

# Input Entered by the User
username = input("ENTER THE NAME: ")
pin = input("ENTER THE PIN: ")
address = input("ENTER YOUR ADDRESS: ")

# Create an account
b = Bank(username, pin, address)

# Display welcome message
b.welcome_message()

# Show transaction menu
b.transaction_menu()
