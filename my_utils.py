#utility functuions for future usage
from datetime import datetime
import random
import string
#for positive and valid number input
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("The number must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input. {e}")
#for date input
def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
#password generator
def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
