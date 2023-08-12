print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

decision_1 = input('You find yourself walking down a spiraling mountain path when you come to a fork in the road, do you want to go left or right?\nEnter "left" or "right": ')
decision_1 = decision_1.lower()

if decision_1 == "right":
    print("You fell down a hole to your doom. Game over!")
elif decision_1 == "left":
    decision_2 = input('You found your way to the bottom of the mountain path and are on the bank of a lake. Do you want to swim or wait?\nEnter "swim" or "wait": ')
    decision_2 = decision_2.lower()

    if decision_2 == "swim":
        print('A giant blue gill eats you as you start to swim in the water. Game over!')
    elif decision_2 == "wait":
        decision_3 = input('After waiting for a while a wizard appears and together you teloport to a small dungeon room with 3 doors. One door is red, the other is blue, and the last door is yellow. Which door do you choose?\nEnter "red", "blue", or "yellow": ')
        decision_3 = decision_3.lower()
        if decision_3 == "red":
            print('You open the red door and flames burst out, surrounding you and burning you to a crisp. Game over goober!')
        elif decision_3 == "blue":
            print('A ginormous swarm of ants bursts out the door and eats you alive. Game over goober!')
        elif decision_3 == "yellow":
            print('Behind the yellow door is like 500 tons of pure gold. You win goober!')
        else:
            print('Make sure to follow instructions goober. Game over!')
    else:
        print('Make sure to follow the instructions goober. Game over!')
else:
    print('Make sure to follow the instructions goober. Game over!')


