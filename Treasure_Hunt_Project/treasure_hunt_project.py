print(''' 
      
      .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
jgs  __||__//
    /.    _/
   // \  /
  //   ||
  \\  /  \
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/
      
      
      ''')

print("Welcome to the Trease Island.\n Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")

direction = input().lower()

if direction == 'left':
    print("Do you want to swim or wait for a boat? Type 'swim' or 'wait'")

    action = input().lower()

    if action == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? Type 'red', 'yellow' or 'blue'")

        door = input().lower()

        if door == 'red':
            print("It's a room full of fire. Game Over.")
        elif door == 'yellow':
            print("You found the treasure! You Win!")
        elif door == 'blue':
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fall into a hole. Game Over.")