import random as r

total_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

my_cards = []
computer_cards = []

# Function to deal cards
def choose_cards(player_cards, iterate: int):
    for _ in range(iterate):
        card = r.choice(total_cards)
        player_cards.append(card)

# Initial 2 cards each
choose_cards(my_cards, 2)
choose_cards(computer_cards, 2)

while True:
    print("\nWelcome to Blackjack 21!")
    print(f"Your cards: {my_cards} (Total = {sum(my_cards)})")
    print(f"Computer shows: [{computer_cards[0]}, ?]")  # hide one card

    # Check if player already busts
    if sum(my_cards) > 21:
        print("You busted! Computer wins 😢")
        break

    # Player's turn
    user_answ = input("Would you like another card? (yes/no): ").lower()

    if user_answ == "yes":
        choose_cards(my_cards, 1)
        continue
    else:
        # Computer's turn: hit until at least 17
        while sum(computer_cards) < 17:
            choose_cards(computer_cards, 1)

        print(f"\nFinal Results:")
        print(f"Your cards: {my_cards} (Total = {sum(my_cards)})")
        print(f"Computer's cards: {computer_cards} (Total = {sum(computer_cards)})")

        # Determine winner
        if sum(computer_cards) > 21:
            print("Computer busted! You win 🎉")
        elif sum(my_cards) > sum(computer_cards):
            print("You win 🎉")
        elif sum(my_cards) < sum(computer_cards):
            print("Computer wins 😢")
        else:
            print("It's a draw 🤝")
        break
