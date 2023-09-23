#Step 4

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

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in range(0, len(chosen_word)):
    display += "_"

space = "_"
while space in display:
    guess = input("Guess a letter: ").lower()
#Check guessed letter
    for letter in range(0, len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess 
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])

    if space not in display:
        print(f"{' '.join(display)}")
        print("You Win")

    if lives == 0:
        print(f"{' '.join(display)}")
        print(f"You lose. The word was {chosen_word}")
        space = "-"
