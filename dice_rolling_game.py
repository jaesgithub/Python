import random

print("Welcome to the Dice Rolling Game!")

while True:
    user_input = input("Roll the dice? (y/n): ")
    if user_input.lower() == "y" or user_input.upper() == "Y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"You rolled a {die1} and a {die2}. Total: {die1 + die2}")
    elif user_input.lower() == "n" or user_input.upper() == "N":
        print("Maybe next time!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")