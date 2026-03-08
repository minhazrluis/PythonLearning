# test utility functions
from my_utils import get_positive_number, get_current_date, generate_password
amount = get_positive_number("Enter a positive number: ")
print(f"You entered: {amount}")
current_date = get_current_date()
print(f"Current date: {current_date}")
password = generate_password(length=16, use_digits=True, use_symbols=False)
print(f"Generated password: {password}")