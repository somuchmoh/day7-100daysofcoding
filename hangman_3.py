#Step 3

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display += "_"
print(display)

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
space = "_"
while space in display:
    if space == "_":
        guess = input("Guess a letter: ").lower()
#Check guessed letter
        for letter in range(0, len(chosen_word)):
            if chosen_word[letter] == guess:
                display[letter] = guess 
        print(display)
print("You Win!")
        