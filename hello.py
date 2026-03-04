#print hello world
print("Hello, World!")

#ask for name
print("what is your name?")
name = input("My name is: ")
print("Hello, " + name + "!")

#ask for birth year to calculate age
birth_year=input("What year were you born? ")
current_year=2026

#check if input year is valid
if birth_year.isdigit():
    birth_year = int(birth_year)
    if current_year>=birth_year>=1900:
        age=current_year-birth_year
        print(f"HELLO {name}, you are {age} years old!")
    else:
        print("Please enter a valid birth year between 1900 and the current year.")
else:
    print("Please enter a valid number for the birth year.")
    
