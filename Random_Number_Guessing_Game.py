import random

play_game = True

while play_game:
  print("Welcome to the Random Number Guessing Game!")
  print("I have selected a random number between 1 and 100.")
  print("Try to guess the number! (Type 'quit' to exit at any time)")
  answer = random.randint(1, 100)
  attempts = 0
  max_attempts = 10
  print(f"You have {max_attempts} attempts to guess the number.")
  quit_game = False

  while attempts < max_attempts:
      try:
          user_input = input("Enter your guess: ")

          if user_input == "quit":
              print("Exiting current game...")
              quit_game = True
              break

          guess = int(user_input)
          attempts += 1

          if guess < 1 or guess > 100:
              print("Please enter an integer between 1 and 100.")
              continue
          if guess < answer:
              print("Too low!")
          elif guess > answer:
              print("Too high!")
          else:
              print(f"Correct! Guessed in {attempts} attempts.")
              break
      except ValueError:
          print("Please enter a number or 'quit' to exit.")

  if attempts >= max_attempts:
      print(f"Game over! Answer was {answer}.")

  play_again = input("Do you want to play again? (y/n) ")
  if play_again.lower() != "y":
    play_game = False
    print("Thanks for playing!")