import random

print(random.randint(1,6))

print(random.random() * 10)

print(random.uniform(1, 10))

random_heads_or_tails = random.randint(0,1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")