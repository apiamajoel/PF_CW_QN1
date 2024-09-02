# ATM Machine Program

# Dictionary to store account information
accounts = {}

# Function to create a new account
def create_account():
    user_id = input("Please enter your user id: ")
    if user_id in accounts:
        print("Account already exists with that ID!")
        return
    password = input("Please enter your password: ")
    accounts[user_id] = {'password': password, 'balance': 0}
    print("Thank you! Your account has been created!")

# Function to log in to an account
def login():
    user_id = input("Please enter your user id: ")
    password = input("Please enter your password: ")
    if user_id in accounts and accounts[user_id]['password'] == password:
        print("Access Granted!")
        return user_id
    else:
        print("*** LOGIN FAILED! ***")
        return None

# Function to show main menu options after login
def main_menu(user_id):
    while True:
        print("\nd -> Deposit Money\nw -> Withdraw Money\nr -> Request Balance\nq -> Quit")
        choice = input("> ").lower()

        if choice == 'd':
            deposit(user_id)
        elif choice == 'w':
            withdraw(user_id)
        elif choice == 'r':
            request_balance(user_id)
        elif choice == 'q':
            print("Thank you for using the ATM Machine. Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

# Function to deposit money
def deposit(user_id):
    amount = float(input("Amount of deposit: $"))
    accounts[user_id]['balance'] += amount
    print(f"${amount} deposited successfully.")

# Function to withdraw money
def withdraw(user_id):
    amount = float(input("Amount of withdrawal: $"))
    if amount > accounts[user_id]['balance']:
        print("Insufficient balance!")
    else:
        accounts[user_id]['balance'] -= amount
        print(f"${amount} withdrawn successfully.")

# Function to request balance
def request_balance(user_id):
    balance = accounts[user_id]['balance']
    print(f"Your balance is ${balance}.")

# Main program loop
def atm_machine():
    print("Hi! Welcome to the ATM Machine!")
    while True:
        print("\nPlease select an option from the menu below:")
        print("l -> Login\nc -> Create New Account\nq -> Quit")
        choice = input("> ").lower()

        if choice == 'l':
            user_id = login()
            if user_id:
                main_menu(user_id)
        elif choice == 'c':
            create_account()
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

# Run the ATM program
atm_machine()
