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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to treasure island")
print("Your mission is to find the treasure")
ans_one = input("You are at the cross road. Where do you want to go?\n\t Type 'Left' or 'Right'.\n")
if ans_one.lower() == "left":
    ans_two = input("You've came to the lake.There is an island in the middle of the lake.\n\t Type 'wait' to wait "
                    "for the boat. Type 'Swim' to swim across.\n")
    if ans_two.lower() == "wait":
        ans_three = input("You've arrived at the island unharmed. There is a house with 3 doors.\n\t One red, one"
                          "yellow and one blue. Which color do you choose?\n")
        if ans_three.lower() == "red":
            print("You've burned by the fire. GAME OVER!!!")
        elif ans_three.lower() == "blue":
            print("You've been eaten by beast. GAME OVER!!!")
        elif ans_three.lower() == "yellow":
            print("YOU WON!!!")
        else:
            print("GAME OVER!!!")
    else:
        print("You've been attacked by the trouts. GAME OVER!!!")
else:
    print("You fall into the hole. GAME OVER!!!")
