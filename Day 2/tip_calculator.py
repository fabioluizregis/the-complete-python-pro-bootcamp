print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $ "))
tip = float(input("How much tip would you like to give? 10, 12 or 15? -> "))
people_to_split = float(input("How many people to split the bill? ->"))

total_per_person = round(float((total_bill+(total_bill*(tip/100)))/people_to_split) , 2)

print(f"Each person should pay: ${total_per_person}")