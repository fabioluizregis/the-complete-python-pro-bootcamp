print("Welcome to Python pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total_price = 0

if size == "S":
    total_price += 15
elif size == "M":
    total_price += 20
else:
    total_price += 25

if pepperoni == "y" and size == "S":
    total_price += 2
elif pepperoni == "Y" and size == "M" or size == "L":
    total_price += 3
else:
    total_price = total_price

if extra_cheese == "Y":
    total_price += 1

print(f"Total price = $ {total_price}")