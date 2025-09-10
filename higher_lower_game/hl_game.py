from celeb_list import celeb_list
from random import randint

already_chosen_indices = []

# Select a random celebrity to start
current_index = randint(0, len(celeb_list) - 1)
current_celeb = celeb_list[current_index]
already_chosen_indices.append(current_index)

def choose_opponent():
    """Select a random celebrity that hasn't been chosen yet and is different from the current one."""
    while True:
        opponent_index = randint(0, len(celeb_list) - 1)
        if opponent_index not in already_chosen_indices and opponent_index != current_index:
            already_chosen_indices.append(opponent_index)
            return celeb_list[opponent_index]

# Main game loop
while True:
    print(f"Current celebrity: {current_celeb['name']}")
    
    opponent_celeb = choose_opponent()
    print(f"Opponent celebrity: {opponent_celeb['name']}")

    user_guess = input("Do you think the opponent has Higher or Lower followers? ").strip().lower()

    if user_guess not in ["higher", "lower"]:
        print("Invalid input. Please type 'Higher' or 'Lower'.")
        continue

    if (user_guess == "higher" and opponent_celeb['follower'] > current_celeb['follower']) or \
       (user_guess == "lower" and opponent_celeb['follower'] < current_celeb['follower']):
        print(f"Correct! {opponent_celeb['name']} has {opponent_celeb['follower']} followers.")
    else:
        print(f"Wrong! {opponent_celeb['name']} has {opponent_celeb['follower']} followers.")
    
    # Update the current celebrity to the opponent for the next round
    current_celeb = opponent_celeb
