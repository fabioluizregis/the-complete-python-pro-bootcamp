# Project - Higher or Lower game!

import random
import database
import logo

score = 0
continue_playing = True

first_famous = database.data_famosos[random.randint(0,100)]

while continue_playing:
    print("\n" * 20)
    print(logo.higher_lower)

    if score != 0:
        print(f"You are right! Current score: {score}")

    second_famous = database.data_famosos[random.randint(0,100)]

    while first_famous == second_famous:
        second_famous = database.data_famosos[random.randint(0,100)]

    print(f"Compare A: {first_famous['name']}, who works as {first_famous['description']} and is from {first_famous['country']}")
    print(logo.versus)
    print(f"Compare B: {second_famous['name']}, who works as {second_famous['description']} and is from {second_famous['country']}")

    followers = input("Who has more followers? Type 'A' or 'B': ").lower()

    a = first_famous['follower_count']
    b = second_famous['follower_count']
    
    if followers == 'a':
        if a > b:
            continue_playing = True
            score += 1
        else:
           continue_playing = False

    if followers == 'b':
        if b > a:
            continue_playing = True
            first_famous = second_famous
            score += 1
        else:
           continue_playing = False

print("\n" * 20)
print(logo.higher_lower)
print(f"Sorry, that`s wrong. Final score: {score}")
print("\n" * 5)