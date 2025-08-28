import random as r
import hangman_char
# list of words
list_of_words=['apple','banana','orange','grapes','lemon','kiwi','mango','pineapple']

# random word
word = r.choice(list_of_words)

display = ['_'] * len(word)

#tries and lives
tries = 0
lives = 6

#result
didWon = False

while tries < lives:
    print(" ".join(display))
    guessed_letter = input("Guess a letter: ").lower()

    for i in range(len(word)):
        if word[i] == guessed_letter:
            display[i] = guessed_letter
        
    if guessed_letter not in display:
        tries += 1
        print(hangman_char.HANGMANPICS[tries])
    

    if "_" not in display:
        didWon = True
        print("You win!🏆")
        break


if not didWon:
    print("You lose!😔")