import csv
from datetime import datetime

# Define file names
INCOME_FILE = 'income_data.csv'
EXPENSE_FILE = 'expense_data.csv'

# Initialize empty lists to store income and expense data
income_data = []
expense_data = []

def load_data():
    """Load income and expense data from CSV files."""
    global income_data, expense_data
    try:
        with open(INCOME_FILE, 'r') as f:
            reader = csv.DictReader(f)
            income_data = list(reader)
    except FileNotFoundError:
        income_data = []

    try:
        with open(EXPENSE_FILE, 'r') as f:
            reader = csv.DictReader(f)
            expense_data = list(reader)
    except FileNotFoundError:
        expense_data = []

def save_data():
    """Save income and expense data to CSV files."""
    with open(INCOME_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['category', 'amount', 'date'])
        writer.writeheader()
        writer.writerows(income_data)

    with open(EXPENSE_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['category', 'amount', 'date'])
        writer.writeheader()
        writer.writerows(expense_data)

def add_income():
    """Add a new income entry."""
    category = input("Enter income category: ")
    amount = float(input("Enter income amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    income_data.append({'category': category, 'amount': amount, 'date': date})

def add_expense():
    """Add a new expense entry."""
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    date = input("Enter date (YYYY-MM-DD): ")
    expense_data.append({'category': category, 'amount': amount, 'date': date})

def view_summary():
    """View the financial summary."""
    total_income = sum(float(entry['amount']) for entry in income_data)
    total_expenses = sum(float(entry['amount']) for entry in expense_data)
    net_savings = total_income - total_expenses

    print(f"\nTotal Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Savings: ${net_savings:.2f}")

def main():
    """Main function to run the Personal Finance Tracker."""
    load_data()

    while True:
        print("\nPersonal Finance Tracker")
        print("1: Add Income")
        print("2: Add Expense")
        print("3: View Summary")
        print("4: Save Data")
        print("5: Load Data")
        print("6: Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            save_data()
            print("Data saved successfully.")
        elif choice == '5':
            load_data()
            print("Data loaded successfully.")
        elif choice == '6':
            save_data()
            print("Exiting and saving data...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

