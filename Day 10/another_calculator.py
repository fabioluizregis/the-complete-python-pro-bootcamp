def add(a , b):
    return a + b

def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b 

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_accumulate = True
    first_number = float(input("What`s the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        pick_operation = input("Pick an operation: ")
        second_number = float(input("What`s the second number?: "))

        answer = operations[pick_operation](first_number, second_number)

        print(f"{first_number} {pick_operation} {second_number} = {answer}")

        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

        if continue_calculation == "y":
            first_number = answer
        else:
            answer = False
            print("\n" * 20)
            calculator()

calculator()