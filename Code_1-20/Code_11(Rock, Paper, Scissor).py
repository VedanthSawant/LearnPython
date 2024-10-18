import random
import MyModule
images = [MyModule.Rock, MyModule.Paper, MyModule.Scissor]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissor\n"))
if user_input > 2:
    print("You have entered wrong input, Please try again!!")
else:
    print(images[user_input])
    comp_input = random.randint(0, 2)
    print(f"Computer chose:\n{images[comp_input]}")
    if user_input == comp_input:
        print("Draw")
    elif user_input == 0 and comp_input == 1:
        print("YOU LOSE")
    elif user_input == 0 and comp_input == 2:
        print("YOU WON")
    elif user_input == 1 and comp_input == 0:
        print("YOU WON")
    elif user_input == 1 and comp_input == 2:
        print("YOU LOSE")
    elif user_input == 2 and comp_input == 0:
        print("YOU LOSE")
    elif user_input == 2 and comp_input == 1:
        print("YOU WON")
