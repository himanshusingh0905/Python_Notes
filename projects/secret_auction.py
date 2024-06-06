logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

# LOGIC:
# function to find highest bid:
def highest_bid(bids):
    highestBid = 0
    winner = ""
    for name in bids:
        if bids[name] > highestBid:
            winner = name
            highestBid = bids[name]
    
    print(f"The winner is {winner} with a bid of ${highestBid}")



# To track bids and bidder-name
bids = {}

bid_again = True
while bid_again:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    # Pushing the bid into dictionary:
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if should_continue == "no":
        bid_again = False
        highest_bid(bids)