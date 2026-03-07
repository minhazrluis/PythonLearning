#number input function
def get_positive_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number <= 0:
                raise ValueError("The number must be positive.")
            return number
        except ValueError as e:
            print(f"Invalid input. {e}")
# Example usage
positive_number = get_positive_number("Please enter a positive number: ")
print(f"You entered: {positive_number}")
    