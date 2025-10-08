from alphabet import alphabet

def decript(text, shift):
    decripted = ""

    for char in text:
        decripted += alphabet[alphabet.index(char)-shift]
    
    print (f"\n\nYour decripted message is: {decripted}")