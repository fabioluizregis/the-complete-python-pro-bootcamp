print("Welcome to the TIP calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people_to_split = int(input("HOw many people will split the bill? "))

total = (total_bill + (total_bill * (tip / 100)))

print(f"Each people should pay: ${round(total / number_of_people_to_split, 2)}")
