#Step 5
from replit import clear
import random
import hangman_art
import hangman_words
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(hangman_words.word_list)
lives = 6
spaces = "_"
guess_list = []

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

print(hangman_art.logo)
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(0, len(chosen_word)):
    display += "_"

space = "_"
while space in display:
    guess = input("Guess a letter: ").lower()
    
    clear()
#Check guessed letter
    for letter in range(0, len(chosen_word)):
        if chosen_word[letter] == guess:
            display[letter] = guess 
    print(display)

    if guess not in chosen_word and guess not in guess_list:
        lives -= 1
        print(f"{guess} is not in the word; \n {hangman_art.stages[lives]}")

    if guess in guess_list:
        print("You guessed this letter already.")
    
    if space not in display:
        print(f"{' '.join(display)}")
        print("You Win")
    
    if lives == 0:
        print(f"{' '.join(display)}")
        print(f"You lose. The word was {chosen_word}")
        space = "-"
    
    guess_list.append(guess) 
