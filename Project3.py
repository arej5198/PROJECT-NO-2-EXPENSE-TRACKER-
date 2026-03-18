expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print("Expense added successfully!")

def view_expenses():
    total = 0
    print("\nYour Expenses:")
    for name, amount in expenses:
        print(name, "-", amount)
        total += amount
    print("Total Expense:", total)

def menu():
    while True:
        print("\n1.Add Expense")
        print("2.View Expenses")
        print("3.Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

menu()