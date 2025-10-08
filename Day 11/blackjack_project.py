from shuffle_cards import shuffle

print("Welcome to PyBlack Jack game!")

user_cards = []
computer_cards = []

play_the_game = input("Lets play? (y/n): ").lower()

for _ in range(2):
        user_cards.append(shuffle())
        computer_cards.append(shuffle())

while(play_the_game == "y"):
    
    print(user_cards)
    print(computer_cards)

    print(f"The sum of user cards = {sum(user_cards)}")
    print(f"The sum of computer cards = {sum(computer_cards)}")

    if sum(user_cards) >= 21 or sum(computer_cards) >= 21:
        if sum(user_cards) == 21:
            play_the_game = "n"
            print("21! User wins!")
        elif sum(computer_cards) == 21:
            play_the_game = "n"
            print("21! Computer wins!")
        else:
             play_the_game = "n"
              
    else:
        play_the_game = input("More cards? (y/n): ").lower()
        user_cards.append(shuffle())
        computer_cards.append(shuffle())

    
if sum(user_cards) % 21 > sum(computer_cards) % 21:
    print(f"User wins with a total of {sum(user_cards)} points! vs {sum(computer_cards)} points computer did!")
else:
    print(f"Computer wins with a total of {sum(computer_cards)} points! vs {sum(user_cards)} points user did!")