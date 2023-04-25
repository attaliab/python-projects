alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#simplified

def caesar(text, shift, direction):
    
    new_word = ""
    for letter in text:
        index = alphabet.index(letter)
        if direction == "encode":
            position = index + shift
        elif direction == "decode":
            position = index - shift
        new_letter = alphabet[position]
        new_word += new_letter
    print(f"The encoded text is {new_word}")


caesar(text, shift, direction)

#Solution above combines the encrypt and decrypt functions
#and if statements into the caesar

# def encrypt(text, shift):
#     new_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         position = index + shift
#         new_letter = alphabet[position]
#         new_word += new_letter
#     print(f"The encoded text is {new_word}")
# 
# 
# def decrypt(text, shift):
#     new_word = ""
#     for letter in text:
#         index = alphabet.index(letter)
#         position = index - shift
#         new_letter = alphabet[position]
#         new_word += new_letter
#     print(f"The decoded text is {new_word}")
# 
# 
# if direction == "encode":
#     encrypt(text, shift)
# if direction == "decode":
#     decrypt(text, shift)
