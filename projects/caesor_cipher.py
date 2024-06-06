# caesor cipher = encoding the plain-text with some operation ( usually by shifting. )

from caesor_cipher_logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(Plain_text, shift_amt):
#     cipher = ""
#     for char in Plain_text:
#         pos = alphabet.index(char)
#         pos = (pos + shift_amt) % 26
#         cipher += (alphabet[pos])
#     return cipher

# def decrypt(plain_text, shift_amt):
#     cipher=""
#     for char in plain_text:
#         pos = alphabet.index(char)
#         pos = (pos - shift_amt + 26) % 26
#         cipher += (alphabet[pos])
#     return cipher
print(logo)

def cipher(plain_text, shift_amt, direction):
    cipher_text = ""
    for char in plain_text:
        pos = alphabet.index(char)
        if direction == "encode":
            pos = (pos + shift_amt) % 26
        else:
            pos = (pos - shift_amt + 26) % 26
        
        cipher_text += alphabet[pos]
    
    return cipher_text



# if __name__ == "__main__":
play = True  # global scope
while play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    print(f"Encrypted text = {cipher(plain_text=text, shift_amt=shift, direction=direction)}")

    if input("Play again? yes or no : ").lower() == "no":
        play = False # still golabal scope

# xyz -> 23,24,25  -> 3 -> 26,27,28 -> %26 = 0,1,2 -> abc
# abc -> 0,1,2 -> 3 -> -3,-2,-1 -> +26 -> 23,24,25 -> %26 -> xyz

# abc -> 0,1,2 -> 3 -> 3,4,5 -> %26 -> 3,4,5 -> def
# def -> 3,4,5 -> 3 -> 0,1,2 -> +26 -> 26,27,28 -> %26 -> abc