import random

choice = int(input("What do you choose? "
                   "Type 0 for Rock,"
                   "1 for Paper or"
                   "2 for Scissors. R:"))

computer = int(random.randint(0,2))

print(choice)
print(computer)

if choice == 0 and computer == 1 :
    print("Paper beats Rock! You Lose!")
elif choice == 0 and computer == 2 :
    print("Rock beats Scissors! You Win!")
elif choice == 1 and computer == 0 :
    print("Paper beats Rock! You Win!")
elif choice == 1 and computer == 2 :
    print("Scissors beats Paper! You Lose!")
elif choice == 2 and computer == 0 :
    print("Rock beats Scissors! You Lose!")
elif choice == 2 and computer == 1 :
    print("Scissors beats Paper! You Win!")
else:
    print("It`s a MATCH!")