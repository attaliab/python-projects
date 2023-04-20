#Step 1
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "babboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for _ in chosen_word:
    display += "_"
print(*display)

end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You Lose")
    print(display)
    if "_" not in display or lives == 0:
        end_of_game = True
        print("You Win")
    
    print(stages[lives])