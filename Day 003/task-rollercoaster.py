print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? R: "))

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("How old are you? R: "))

    if age < 12:
        print("You pay $5!")
    elif age >= 12 and age <= 18:
        print("You pay $7!")
    else:
        print("You pay $12!")
else:
    print("Sorry, you have to grow taller before you can ride!")