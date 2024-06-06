
from game_data import data
from game_art import logo, vs

import random


############     flow:
# choose 2 players
# compare followers 
# if guess is right get to play more
# else game ends and score is shown

print(logo)

length = len(data)
score = 0
guess = True
while guess:
    A = random.randint(0,length-1)
    B = random.randint(0,length-1)
    print(f"Compare A : {data[A]['name']}, {data[A]['description']}, from {data[A]['country']}")
    print(vs)
    print(f"Against B : {data[B]['name']}, {data[B]['description']}, from {data[B]['country']}")

    yourGuess = input("Who has more followers? Type 'A' or 'B' : ").upper()
    if data[A]['follower_count'] > data[B]['follower_count']:
        correctAns= "A"
    else:
        correctAns = "B"

    if yourGuess == correctAns:
        score += 1
        print(f"You are right! and Current Score = {score}")
    else:
        # game over
        guess = False
        print(f"Sorry, that's wrong. Final score : {score}")

