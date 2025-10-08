from alphabet import alphabet

def encript(text, shift):
    encripted = ""

    for char in text:
        if alphabet.index(char)+shift > len(alphabet):
            new_index = alphabet.index(char)+shift - len(alphabet)
            encripted += alphabet[new_index]
        else:
            encripted += alphabet[alphabet.index(char)+shift]
    
    print (f"\n\nYour encripted message is: {encripted}")