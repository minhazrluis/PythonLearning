# simple calculator with while loop
while True:
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ['1', '2', '3', '4']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        if choice == "1":
            print(f"{a} + {b} = {a+b}")
        elif choice == "2":
            print(f"{a} - {b} = {a-b}")
        elif choice == "3":
            print(f"{a} * {b} = {a*b}")
        elif choice == "4":
            if b != 0:
                print(f"{a} / {b} = {a/b}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Exiting the calculator. Goodbye!")
        break