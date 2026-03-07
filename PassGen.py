#password generator
import random
import string
#length input error handling
def length_input(prompt):
    while True:
        try:
            length = int(input(prompt))
            #length must be greater than 8 and less than 128
            if length < 8 or length > 128:
                print("Length must be between 8 and 128. Please try again.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
#include digits?
def include_digits():
    while True:
        choice = input("Include digits? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
#include letters?
def include_letters():
    while True:
        choice = input("Include letters? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
#include special characters?
def include_special_characters():
    while True:
        choice = input("Include special characters? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    while True:
        print("Welcome to the Password Generator!")
        length = length_input("Enter the desired password length (8-128): ")
        use_digits = include_digits()
        use_letters = include_letters()
        use_special_characters = include_special_characters()
        if not use_digits and not use_letters and not use_special_characters:
            print("You must include at least one character type (digits, letters, or special characters). Please try again.")
            continue
        characters = ""
        if use_digits:
            characters += string.digits
        if use_letters:
            characters += string.ascii_letters
        if use_special_characters:
            characters += string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated password: {password}")
        break
if __name__ == "__main__":
    main()