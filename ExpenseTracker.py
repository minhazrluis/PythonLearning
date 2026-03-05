#Expense Tracker
import json
expenses = []
#save expenses to file
def save_expenses():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)
#load expenses from file
def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
#add expense
def add_expense(name, amount, category):
    expense = {
        'name': name,
        'amount': amount,
        'category': category
    }
    expenses.append(expense)
    save_expenses()
    print(f"Expense {name} added successfully.")
#view expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
    else:
        for i, expense in enumerate(expenses, start=1):
            print(f"Expense {i}:")
            print(f"  Name: {expense['name']}")
            print(f"  Amount: {expense['amount']}")
            print(f"  Category: {expense['category']}")
#total spent
def total_spent():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total spent: {total}")
#main function
def main():
    global expenses
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter expense name: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(name, amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_spent()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    