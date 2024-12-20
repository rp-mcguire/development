#This is a practice script written in python. It is a number guessing game.
#
#
#import dependencies
import random

# welcome user to game, explain rules
print("Hi, welcome to the game. This is a number guessing game.\nYou have seven chances to guess the number. Let's start the game")

#get user input for the start and end of the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# generate user defined range
num_to_guess = random.randrange(start, end)

chances = 7

guess_count = 0

while guess_count < chances:
    guess_count += 1
    user_guess = int(input("Enter a guess: "))
    if user_guess == num_to_guess:
        print("Good Job! You guessed the number!")
        break
    elif guess_count >= chances and user_guess !=  num_to_guess:
        print("You didn't guess the number in 7 chances. The number was " + str(num_to_guess))
    elif user_guess > num_to_guess:
        print("Your guess is too high.")
    elif user_guess < num_to_guess:
        print("Your guess is too low.")

    
