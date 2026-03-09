#cli tools
import sys
import json
from my_utils import get_current_date, generate_password
#add expense
def add_expense(name, amount, category):
    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": get_current_date()
    }
    with open("expenses.json", "a") as f:
        json.dump(expense, f)
        f.write("\n")
    print("Expense added successfully!")
#view expenses
def view_expenses():
    try:
        with open("expenses.json", "r") as f:
            expenses = [json.loads(line) for line in f]
            for expense in expenses:
                print(f"{expense['date']}: {expense['name']} - ${expense['amount']} ({expense['category']})")
    except FileNotFoundError:
        print("No expenses found.")
#total spent
def total_spent():
    total = 0
    try:
        with open("expenses.json", "r") as f:
            expenses = [json.loads(line) for line in f]
            total = sum(expense["amount"] for expense in expenses)
    except FileNotFoundError:
        print("No expenses found.")
    print(f"Total spent: ${total}")
def main():
    if len(sys.argv) < 2:
        print ("usage: python cli_tool.py [add/view/total/password]")
        return
    command = sys.argv[1]
    if command == "add":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        add_expense(name, amount, category)
    elif command == "view":
        view_expenses()
    elif command == "total":
        total_spent()
    elif command == "password":
        password = generate_password(length=16, use_digits=True, use_symbols=False)
        print(f"Generated password: {password}")
    else:
        print("Unknown command. Use add/view/total/password.")
if __name__ == "__main__":
    main()