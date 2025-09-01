print('Welcome to the secret auction program.')

bidders = {}
while True:
    name = str(input('What is your name?: '))
    bid = int(input('What is your bid?: $'))
    bidders[name] = bid
    more_bidders = input('Are there any other bidders? Type "yes" or "no": ')
    if more_bidders == 'no' or more_bidders != 'yes':
        break

def find_highest_bidder(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        
        bid_amount = bidders[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


find_highest_bidder(bidders)
