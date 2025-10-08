

from select_difficulty import select_difficulty
from choose_number import choose_a_number
from logo import logo

lets_play = True

while lets_play:
    print("\n" * 20)
    print(logo())
    print("Welcome to the Number Guessing Game!")
    print("I`m thinking on a number between 1 and 100.")

    secret_number = choose_a_number()
    game_over = False

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = select_difficulty(difficulty)

    while not game_over and attempts != 0:
        
        print(f"You have {attempts} attempts remaining to guess the number.")
        your_guess = int(input("Make a guess: "))
        
        if your_guess == secret_number:
            print(f"You found the number!!")
            game_over = True

        elif attempts == 1:
            print("That was your last attempt and you couldn`t find the number")
            print(f"The correct number was {secret_number}")
            game_over = True

        elif your_guess > secret_number:
            attempts -= 1
            print("Too high.\nGuess again.")

        else:
            attempts -= 1
            print("Too low.\nGuess again.")

    do_it_again = input("Do you want to try again? 'y' or 'n'?: ").lower()
    
    if do_it_again == "n":
        lets_play = False
  