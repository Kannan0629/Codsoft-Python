def calculator():
    print("Simple Calculator")
    print("------------------")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("Choose an operation:")
        print(" + : Addition")
        print(" - : Subtraction")
        print(" * : Multiplication")
        print(" / : Division")

        operation = input("Enter your choice (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation choice.")
    
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Run the calculator
calculator()
