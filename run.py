import random

# Welcome message to my application
# Present user with options with which program they would like to run 
# User makes choice with input and respective program begins
# At the end of each program, the computer will ask the user if they 
# would like to return to this 'menu' or run the program again


# User has to guess a number generated by the computer


def guessing_function():
    """
    A function that generates a random number and upon
    user input guesses, generates an automatic response.
    Ends when the user correctly guesses the number.

    """

    random_number_100 = random.randint(1, 101)

    try:
        user_guess = int(input("Guess an integer between 1 and 100: "))
        while random_number_100 != user_guess:
            if user_guess > 100 or user_guess < 1:
                print(f"You can't choose {user_guess}\n")
                print("Please pick an integer between 1 and 100 only!")
                pass
                user_guess = int(input("Guess an integer between 1 and 100: "))

            elif user_guess > random_number_100:
                print("Too high, try a bit lower!")
                user_guess = int(input("Guess an integer between 1 and 100: "))
            elif user_guess < random_number_100:
                print("Too low, try a bit higher!")
                user_guess = int(input("Guess an integer between 1 and 100: "))

        print(f"You got it! The number was: {random_number_100}")

    except ValueError:
        print("Wrong value! Please enter a number between 1 and 100!")
        guessing_function()


guessing_function()


# Computer has to guess a number generated by the User

# User chooses a number
# Computer makes a guess
# User gets an input to say if the number needs to be lower or higher 
# by entering 1 for lower, 2 for higher or 3 for when the number is correct
# Continues until computer gets to the correct number
# prompt to play again or something else

def comp_guessing_function():

    """
    A function that generates a random number guess between
    two variables of value 1 and 101, and upon user input, 
    adjusts the next guess based on whether the user feedback
    requires a higher or lower number.
    """

    print("Pick a number between 1 and 100, and I'll try to guess it!")

    min = 1
    max = 101

    user_response = ""
    while user_response != 3:
        computer_guess = random.randint(min, max)
        user_response = int(input("If I'm too low, press 1. Too high, press 2. If I'm spot on, press 3!"))
        if user_response == 1:
            min = computer_guess + 1
        elif user_response == 2:
            max = computer_guess - 1
    print("Hoorah! I guessed your number")


comp_guessing_function()


# Coin Toss (Heads/Tails)

# Program begins when user presses a key
# User calls in an input whether they think it will be heads or tails
# The computer makes a guess of its own
# The 'coin' is flipped and a result is generated
# See who wins the round
# Prompt to either 'flip a coin' again or do something else