import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
           'O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','+']

print("Welcome to the password generator!")

number_of_letters = int(input("How manu letters would you like on your password? R: "))
number_of_numbers = int(input("How many numbers would you like on your password? R: "))
number_of_symbols = int(input("How many symbols would you like on your password? R: "))

password = ""

for char in range(1, number_of_letters + 1):
    random_char = random.choice(letters)
    password += random_char

for number in range(1, number_of_numbers + 1):
    random_number = random.choice(numbers)
    password += str(random_number)

for symbol in range(1, number_of_symbols + 1):
    random_symbol = random.choice(symbols)
    password += str(random_symbol)

print(password)

scramble = []
for char in password:
    scramble.append(char)

random.shuffle(scramble)

password_scrambled = ""
for char in scramble:
    password_scrambled += char

print(password_scrambled)