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

alleyway = input("You have come across an alleyway! Do you want to choose left or right: ")
alleyway_lower = alleyway.lower()
if alleyway_lower == "left":
    second_stage = input("You have passed the alleyway. You have come across a river! Swim or wait: ")
    second_stage_lower = second_stage.lower()
    if second_stage_lower == "wait":
        third_stage = input("You have arrived at a dead end! Choose a door: Yellow, Red, or Blue: ")
        third_stage_lower = third_stage.lower()
        if third_stage_lower == "red":
            print("You have been burned by fire. Game over!")
        elif third_stage_lower == "blue":
            print("You have been eaten by a beast. Game over!")
        elif third_stage_lower == "yellow":
            print("You win! Champion!")
        else:
            print("Game over!")
    else:
        print("You have been attacked by trout. Game over!")
else:
    print("You have fallen into an enemy death trap! Game over!")
