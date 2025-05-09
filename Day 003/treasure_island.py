print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")

option = input("Left or Right? R: ").upper()

if option == "RIGHT" :
    print("Game Over!")
else:
    option = input("Swim or Wait? R: ").upper()
    if option == "SWIM":
        print("Game Over!")
    else:
        option = input("Witch door? Red, Blue or Yellow? R: ").upper()
        if option == "RED" or option == "BLUE" :
            print("Game Over!")
        else:
            print("You Win!")