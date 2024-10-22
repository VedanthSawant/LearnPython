# Write a program for number guessing game.
# First computer will generate a random number and user need to guess this number.

import MyModule, random

def playGame(life_left):
    comp_num = random.randint(1, 101)
    while life_left > 0:
        print(f"You have {life_left} attempts remaining to guess a number.")
        user_num = int(input("Make a guess: "))
        if user_num == comp_num:
            life_left = 0
            print(f"You got it. The answer was {comp_num}")
        elif user_num > comp_num:
            life_left -= 1
            print("Too high.")
        else:
            life_left -= 1
            print("Too low.")

user_input = "y"
while user_input == "y":
    print(MyModule.number_logo)
    print("Welcome to the Number Guessing Game!")
    print("I\'m thinking of a number between 1 to 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        playGame(10)
    elif level == "hard":
        playGame(5)
    else:
        print("Please type correctly!!!")
    user_input = input("Do you want to play the Number Guessing Game? Type 'y' for YES or 'n' for NO.: ")