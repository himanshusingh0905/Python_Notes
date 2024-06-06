
# flow_diagram:
# 1. generate a random word
# 2. ask user to guess a letter
# 3. if it's in the word, then fill the blank and check if all letters are guessed. 
# 4. if it's not in the word, then reduce life of hangman by 1. and check if all lives are gone.
# 5. from step 3 or 4, if it's true, then -> game over
# 6. If not true, then ask user to guess again a new word.

import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
lives = 6

# Let's create a list containing blanks
blanks = ["_" for i in range(word_length)]
# printing hangman logo
print(logo)

while "_" in blanks and lives > 0:
    letter = input("Guess a letter : ").lower()
    if letter in blanks:
        print("Already guessed..")
        continue

    if letter in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == letter:
                blanks[i] = letter
        print( " ".join(blanks))

    else:
        lives -= 1
        print("Oops! Wrong letter....")
        print(stages[lives])

# printing final results
if lives == 0 :
    print("GAME OVER")
    print("You Lost")
else:   
    print(f"Congratulations, You Won")
    print(f"Here is your word : {''.join(blanks)}")
