
import random
from number_guessing_art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
number = random.randint(1,100)

if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

while attempts:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        Print("You have got it right. the answer is {guess}")
        break

    attempts -= 1
    print("Guess again")
