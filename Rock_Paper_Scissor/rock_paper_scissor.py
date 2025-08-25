import random as r
# Symbols 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]

print("Rock, Paper, Scissor Game")

print("Enter your choice\n 1.Rock\n 2.Paper\n 3.Scissor\n")

choice = int(input("Enter your choice: "))


print("Your choice: ", choice)

print(image[choice-1])


computer = r.randint(1,3)

print("Computer choice: ", computer)

print(image[computer-1])


if choice == computer:
    print("Tie")

elif choice == 1 and computer == 2:
    print("You lose")

elif choice == 1 and computer == 3:
    print("You win")

elif choice == 2 and computer == 1:
    print("You win")

elif choice == 2 and computer == 3:
    print("You lose")

elif choice == 3 and computer == 1:
    print("You lose")

elif choice == 3 and computer == 2:
    print("You win")