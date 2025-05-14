import random
import hangman_words

# TODO 1 - Randomly choose a word from word_list and assign it to a variable called chosen_word. Then print it.

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
for char in chosen_word:
    placeholder += "_"

print(placeholder)
# TODO 2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

game_over = False
correct_letters = []

lives = 6

while not game_over:
    guess = input("Guess a letter! R:").lower()
    print(guess)

    # TODO 3 - Check if the letter the user guessed is one of the letters in the chosen_word.
    #          Print "Right" if it is correct
    #          Print "Wrong" if it is not correct


    display = ""

    if guess not in chosen_word:
        lives -= 1

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    print(f"Vidas = {lives}")

    if "_" not in display:
        game_over = True
        print("You Win!")
        break

    if lives == 0:
        print("You LOSE!")
        print(f"The correct word was: {chosen_word}")
        break