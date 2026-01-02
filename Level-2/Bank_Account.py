import json
import os

FILE_NAME = "bank_data.json "

# Load account data
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        account = json.load(file)

else:
    account = None

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(account, file)

while True:
    print("\n🏦 Simple Bank Account System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    # CREATE ACCOUNT
    if choice == "1":
        if account is not None:
            print("❗ Account already exists.")
        else:
            name = input("Enter your name: ")
            acc_no = input("Enter account number: ")
            balance = float(input("Enter initial deposit: "))

            if balance < 0:
                print("❌ Balance cannot be negative.")
            else:
                account = {
                    "name": name,
                    "account_number": acc_no,
                    "balance": balance
                }
                save_data()
                print("✅ Account created successfully.")

    # DEPOSIT
    elif choice == "2":
        if account is None:
            print("❗ Create an account first.")
        else:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("❌ Invalid amount.")
            else:
                account["balance"] += amount
                save_data()
                print("✅ Amount deposited.")

    # WITHDRAW
    elif choice == "3":
        if account is None:
            print("❗ Create an account first.")
        else:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("❌ Invalid amount.")
            elif amount > account["balance"]:
                print("❌ Insufficient balance.")
            else:
                account["balance"] -= amount
                save_data()
                print("✅ Withdrawal successful.")

    # CHECK BALANCE
    elif choice == "4":
        if account is None:
            print("❗ No account found.")
        else:
            print("\n📄 Account Details")
            print("Name:", account["name"])
            print("Account Number:", account["account_number"])
            print("Balance: ₹", account["balance"])

    # EXIT
    elif choice == "5":
        print("👋 Thank you for using the Bank System.")
        break

    else:
        print("❗ Invalid choice. Try again.")




