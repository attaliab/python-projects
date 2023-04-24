alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
    if direction == encode
    if direction == decode




#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.



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
