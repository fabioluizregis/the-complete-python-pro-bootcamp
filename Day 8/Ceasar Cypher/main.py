from encript import encript
from decript import decript

print("Welcome to Ceasar Cypher!!")

keep_working = True

while (keep_working):

    encode_or_decode = input("What do you want to do?\n" \
    "- Type 'encode' to encode a message. \n" \
    "- Type 'decode' to decode a message. \n" \
    "- Type 'quit' to quit the Ceasar Cypher. \n" \
    "- Answer: ").lower()

    if encode_or_decode == 'encode':
        message = input("Type your message to encrypt: ")
        shift = int(input("Type your shift secret number: "))

        encript(message, shift)
        
    elif encode_or_decode == 'decode':
        message = input("Type your message to encrypt: ")
        shift = int(input("Type your shift secret number: "))

        decript(message, shift)
    else:
        keep_working = False
        print("Thanks for using Ceasar Cypher!")

