import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def anotherCard(hands, score):
    randomCard = random.choice(cards)
    if randomCard == 11 and score + randomCard > 21:
        score += 1
        hands.append(1)
    else:
        hands.append(randomCard)
        score += randomCard
    return hands,score

def playBlackjack():
    my_cards = []
    my_cards.append(random.choice(cards))
    my_cards.append(random.choice(cards))

    computer_cards = []
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    computer_sum = sum(computer_cards)
    my_sum = sum(my_cards)

    if my_sum > 21:
        my_cards[1] = 1
        my_sum = 12
    if computer_sum > 21:
        computer_cards[1] = 1
        computer_sum = 12

    print(f"Your cards: {my_cards}, current score : {my_sum}")
    print(f"Computer's first card : {computer_cards[0]}")

    if computer_sum== 21: 
        print(f"Your final hand : {my_cards}")
        print(f"Computer's final hand : {computer_cards}")
        print("Computer won by Blackjack")
        return
    elif my_sum==21:
        print(f"Your final hand : {my_cards}")
        print(f"Computer's final hand : {computer_cards}")
        print("You won by Blackjack")
        return


    # For user
    takeAnotherCard = input("Take another card, Type 'y' or 'n': ").lower()
    while takeAnotherCard == "y":
        my_cards,my_sum = anotherCard(my_cards,my_sum)
        if my_sum > 21:
            print(f"Your final hand : {my_cards}")
            print(f"Computer's final hand : {computer_cards}")
            print("You went over, You lose")
            return
        print(f"Your cards: {my_cards}, current score : {my_sum}")
        print(f"Computer's first card : {computer_cards[0]}")
        tempCard = input("Take another card, Type 'y' or 'n': ").lower()
        takeAnotherCard = tempCard
    # for computer:
    while computer_sum <= 16:
        computer_cards,computer_sum = anotherCard(computer_cards,computer_sum)
        if computer_sum > 21:
            print(f"Your final hand : {my_cards}")
            print(f"Computer's final hand : {computer_cards}")
            print("Computer went over, You Win")
            return
        elif computer_sum== 21: 
            print(f"Your final hand : {my_cards}")
            print(f"Computer's final hand : {computer_cards}")
            print("Computer won by Blackjack")
            return

    if my_sum > computer_sum:
        print(f"Your final hand : {my_cards}")
        print(f"Computer's final hand : {computer_cards}")
        print("You Win")
    elif my_sum == computer_sum:
        print(f"Your final hand : {my_cards}")
        print(f"Computer's final hand : {computer_cards}")
        print("It's a draw")
    else:
        print(f"Your final hand : {my_cards}")
        print(f"Computer's final hand : {computer_cards}")
        print("You lose")



while input("Do you want play a game of Blackjack? Type 'y' or 'n' : ").lower() == "y":
    playBlackjack()
    print("-----------------------------------------------------------------------------")

    


# def compare(user_score, computer_score):
#   #Bug fix. If you and the computer are both over, you lose.
#   if user_score > 21 and computer_score > 21:
#     return "You went over. You lose 😤"


#   if user_score == computer_score:
#     return "Draw 🙃"
#   elif computer_score == 0:
#     return "Lose, opponent has Blackjack 😱"
#   elif user_score == 0:
#     return "Win with a Blackjack 😎"
#   elif user_score > 21:
#     return "You went over. You lose 😭"
#   elif computer_score > 21:
#     return "Opponent went over. You win 😁"
#   elif user_score > computer_score:
#     return "You win 😃"
#   else:
#     return "You lose 😤"