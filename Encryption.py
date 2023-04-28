alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
        
if shift > 26:
    shift = shift % 26


def caesar(text, shift, direction):
    new_word = ""
    for char in text:
        if char not in alphabet:
            new_word += char
        else:
            index = alphabet.index(char)
            if direction == "encode":
                position = index + shift
            elif direction == "decode":
                position = index - shift
            new_char = alphabet[position]
            new_word += new_char
    print(f"The encoded text is {new_word}")

    
caesar(text, shift, direction)
restart = (input("Would you like to restart? "))
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = (input("Would you like to restart? "))
    if restart == "no":
        print("Goodbye")
