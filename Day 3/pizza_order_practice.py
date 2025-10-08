print("Welcome to Python Pizza Deliveries!")
size = (input("What size pizza do you want? S, M or L : ")).upper()
pepperoni = (input("Do you want pepperoni on your pizza? Y or N : ")).upper()
extra_cheese = (input("Do you want extra cheese? Y or N : ")).upper()

price = 0

if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20
    if pepperoni == "Y":
        price += 3
else:
    price += 25
    if pepperoni == "Y":
        price += 3

if extra_cheese == "Y":
    price += 1

print(f"The total cost of your pizza is ${price}")





