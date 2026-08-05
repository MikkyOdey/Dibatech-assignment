import random

play_again = "yes"

while play_again == "yes":

    # Generate a random number
    secret_number = 3

    # Ask the user to guess
    guess = int(input("\nI'm thinking of a number between 1 and 10. Can you guess it? "))

    # Check if the guess is correct, too high, or too low
    if guess == secret_number:
        result = "correct"
    elif guess > secret_number:
        result = "high"
    else:
        result = "low"

    # Display the result using match-case
    match result:
        case "correct":
            print("Congratulations, you guessed it!")
            break
        case "high":
            print("Oops, your guess is a bit high. Try again!")
        case "low":
            print("Nope, your guess is a bit low. Give it another shot!")

    # Ask the user if they want to play again
    play_again = input("Play again? (yes/no): ").lower()

print("Thanks for playing!")