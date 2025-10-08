import random
from list_of_words import word_list

lives = 6

random_word = random.choice(word_list)

creating_blanks = ""

for letter in range(1, len(random_word)+1):
    creating_blanks += "_"

print(random_word)
print(creating_blanks)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in display:
        lives -= 1

    print(display)
    print(lives)

    if "_" not in display:
        game_over = True
        print("You Win!")
    
    if lives == 0:
        game_over = True
        print("You Lose!")