import random as r

numbers = []
for i in range(1,101):
    numbers.append(i)

# alternate to use the random value 
# import ranint from random , ==> answer = randint(starting_int,ending_int)

picking_up_number = r.choice(numbers)
leval_low_tries = 5
level_upgrade_tries = 10

print("Welcome to the game bitch!")
user_answ = input('Enter the level you wana play  easy or hard bitch? easy or hard ')


game_over = False


def game_engine(tries: int)-> bool:
    print(f'Bitch you have got {tries} chances?')
    while tries != 0:
            guess = int(input("My guess is:  "))
            tries -= 1
            if guess != picking_up_number:
                if picking_up_number > guess:
                    print('Your number is smaller than guessed number !')
                else:
                     print('Your number is greater than guessed number !')
                continue
            else:
                print('You have got it bitch!!')
                return True
    return False



while not game_over:
    if user_answ == 'easy':
       game_over = game_engine(tries=leval_low_tries)
    elif user_answ == 'hard':
       game_over = game_engine(tries=level_upgrade_tries)
    else:
        break
        


