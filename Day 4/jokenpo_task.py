import random


choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. => "))

choices = ["Rock", "Paper", "Scissors"]

computer_choice = random.randint(0, 2)

# print(choices[choice] + "  " + choices[computer_choice])

if (choice == 0 and computer_choice == 1):
    print(f"You lose! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")
elif (choice == 0 and computer_choice == 2):
    print(f"You won! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")
elif (choice == 1 and computer_choice == 0):
    print(f"You won! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")
elif (choice == 1 and computer_choice == 2):
    print(f"You lose! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")
elif (choice == 2 and computer_choice == 0):
    print(f"You won! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")    
elif (choice == 2 and computer_choice == 1):
    print(f"You won! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")
else:
    print(f"It`s a match! Your choice is {choices[choice]} and the computer choose {choices[computer_choice]}")