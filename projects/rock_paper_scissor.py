import random
event = ['''rock:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

''',

'''paper:
    _________
---'   ______)____
          ________)
          _________)
         ________)
---.____________)

''',

'''scissor:
     _
    | |
---'  |________
          ______)
       __________)
      (____)
---.__(___)
''']

def game():
    # Getting user's input : 
    user = None
    valid_input = False
    while not valid_input:
        try:
            user = int(input("Enter your choice: 0 for paper, 1 for scissor, 2 for rock : "))
            if user > 2 or user <0 :
                print("Invalid input..........\n")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input..........\n")

    print("You chose:")
    print(event[user])

    comp = random.choice(range(0,3))
    print("Computer chose:")
    print(event[comp])

    # Logic
    if user==0 and comp==2:
        print("You Win")
        return 1
    elif user==2 and comp==0:
        print("You Lose")
        return 0
    elif user > comp:
        print("You Win")
        return 1
    elif user < comp:
        print("You Lose")
        return 0
    else:
        print("Draw")
        return None


if __name__ == "__main__":
    print("Let's play the game of ROCK-PAPER and SCISSOR")

    play = True
    # to track total game played
    total = 1
    score = 0
    draw = 0
    # count to track score
    val = game()
    if val: 
        score += 1
    elif val == None:
        draw += 1

    while play:
        print("PLAY AGAIN? choose y or n:")
        check = input() # y or n
        # if  n  -> then no call to the game()
        if check == "y":
            total += 1
            temp = game()
            if temp:
                score += 1
            elif temp == None:
                draw +=  1
        else:
            play = False

    print(f"Total match played = {total}")
    print(f"Draws = {draw}")
    print(f"SCORE = {score} - {total-draw-score}")


