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

for char in range(1,number_of_letters + 1):
    password += random.choice(letters)

for char in range(1,number_of_numbers + 1):
    password += random.choice(numbers)

for char in range(1,number_of_symbols + 1):
    password += random.choice(symbols)

print(password)

def shuffle_string(s):
    char_list = list(s)
    random.shuffle(char_list)
    return ''.join(char_list)

string_embaralhada = shuffle_string(password)
print(string_embaralhada)