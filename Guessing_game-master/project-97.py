import random

# Print the rules and idea of the game
print("This is a number guessing game. You will guess a number between 1 and 9 and if it comes our correct, you win. You will have five chances for the same")

# Generate a random number between 1 and 9 and store it in number variable
number = random.randint(1, 9)

# Variable chances holds the number of chances the user gets to guess the number
chances = 0

#Telling the user to guess the number
print("Guess a number between 1 and 9")

#While loop to give user 5 chances and check if it was correct or close
while chances < 5:
    guess = int(input("Enter your guess :- "))

    # If guess is correct
    if guess == number:
        print("CONGRATULATIONS!!! YOU GUESSED THE NUMBER")
        break

    # If guess greater than number
    elif guess > number:
        print("You guess was too high, try a number lower than ",guess)
    
    # If guess less than number
    else:
        print("You guess was too low, try a number higher than ",guess)

    # Incrementing the value of chances variable
    chances += 1

# If all five guesses were wrong, reveal the number
if not chances < 5:
    print("YOU LOSE :( THE NUMBER WAS - ",number)