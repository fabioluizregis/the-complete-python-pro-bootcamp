def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

answer = True

print("Calculator!")

first_number = float(input("What`s the first number?: "))
print("+\n-\n*\n/")
pick_operation = input("Pick an operation: ")
second_number = float(input("What`s the second number?: "))

while answer:
    if pick_operation == "+":
        result = add(first_number, second_number)
        print(f"{first_number} + {second_number} = {result}")
        first_number = result
    
    if pick_operation == "-":
        result = subtract(first_number, second_number)
        print(f"{first_number} - {second_number} = {result}")
        first_number = result
    
    if pick_operation == "*":
        result = multiply(first_number, second_number)
        print(f"{first_number} * {second_number} = {result}")
        first_number = result

    if pick_operation == "/":
        result = divide(first_number, second_number)
        print(f"{first_number} / {second_number} = {result}")
        first_number = result

    continue_calculation = input(f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ").lower()

    if continue_calculation == "y":
        print("+\n-\n*\n/")
        pick_operation = input("Pick an operation: ")
        second_number = float(input("What`s the second number?: "))
    else:
        answer = False