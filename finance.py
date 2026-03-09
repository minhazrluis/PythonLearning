#finance tracker using finance_utility_func.py and build a command line interface for it

import sys
from finance_utility_func import add_expenses, view_expenses, total_spent, validate_positive_amount, export_expenses_to_csv
def main():
    if len(sys.argv) < 2:
        print("Usage: python finance.py [add/view/total/export]")
        return
    command = sys.argv[1]
    if command == "add":
        name = input("Enter expense name: ")
        amount_input = input("Enter expense amount: ")
        amount = validate_positive_amount(amount_input)
        if amount is not None:
            category = input("Enter expense category: ")
            add_expenses(name, amount, category)
            print("Expense added successfully!")
    elif command == "view":
        view_expenses()
    elif command == "total":
        total_spent()
    elif command == "export":
        export_expenses_to_csv()
        print("Expenses exported to expenses.csv successfully!")
    else:
        print("Unknown command. Use add/view/total/export.")
if __name__ == "__main__":
    main()