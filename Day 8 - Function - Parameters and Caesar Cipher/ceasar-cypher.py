alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
            'p','q','r','s','t','u','v','w','x','y','z']

print(len(alphabet))

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def encode(text, shift):
    new_text = ""
    for letter in text:
        letter_position = alphabet.index(letter)
        new_text += alphabet[(letter_position+shift) % len(alphabet)]

    print(new_text)


def decode(text, shift):
    new_text = ""
    for letter in text:
        letter_position = alphabet.index(letter)
        new_text += alphabet[(letter_position-shift) % len(alphabet)]

    print(new_text)

if direction == "encode":
    encode(text,shift)
else:
    decode(text,shift)

