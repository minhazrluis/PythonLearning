#a finamce related utility function
from datetime import datetime
import json
import csv
#save expenses in json format
def save_expenses_to_json(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)
#load expenses from json file
def load_expenses_from_json():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

#add expense with date and save to json file
def add_expenses(name, amount, category):
    expenses = load_expenses_from_json()
    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    expenses.append(expense)
    save_expenses_to_json(expenses)
#view expenses with date
def view_expenses():
    expenses = load_expenses_from_json()
    if not expenses:
        print("No expenses found.")
        return
    for expense in expenses:
        print(f"{expense['date']}: {expense['name']} - ${expense['amount']} ({expense['category']})")
#positive input validation for amount
def validate_positive_amount(amount):
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError("Amount must be a positive number.")
        return value
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

#total spent
def total_spent():
    expenses = load_expenses_from_json()
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total spent: {total}")
#export expenses to csv file
def export_expenses_to_csv():
    expenses = load_expenses_from_json()
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Amount", "Category", "Date"])
        for expense in expenses:
            writer.writerow([expense["name"], expense["amount"], expense["category"], expense["date"]])