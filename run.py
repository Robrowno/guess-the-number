"""
Main app file for game
"""
import random
import os

import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


class Helper:

    """
    A class to represent common handlers present on some or all games
    in the application.
    """

    def __init__(self):
        pass

    def get_dict_key(self, dictionary, value):
        """
        This returns the key name from an inputted value
        """

        return list(dictionary.keys())[list(dictionary.values()).index(value)]

    def get_int(self, string):
        """
        Function that handles user input for different numbers. As long as
        the input value is determined to be an integer, it is returned.
        Otherwise, a ValueError is raised to print the message below.
        """
        while True:
            try:
                return int(input(string))

            except ValueError:
                print(f"\n{Fore.RED}Not an integer, try again\n")

    def clear_terminal(self):
        """
        This function will clear the terminal at the end of a program
        round in order to prevent the terminal from becoming too long
        and cluttered. "posix" is the term referring to Linux or
        MacOS operating systems. "nt, dos and ce" are for DOS or Windows
        operating systems.
        """
        if os.name == "posix":
            os.system("clear")
        elif os.name in ("nt", "dos", "ce"):
            os.system("CLS")
        else:
            print("\n" * 150)


class PlayerGuesses(Helper):

    """
    This class represents the first game, Guess-The-Number.
    The game is accessed through the play() function below.
    """

    def __init__(self):
        super().__init__()
        self.guesses = 0

    def play(self):
        """
        A function that generates a random number and upon
        user input guesses, generates an automatic response.
        Ends when the user correctly guesses the number.
        """

        random_number_100 = random.randint(1, 101)
        self.guesses = 0
        user_guess = self.get_int("\nGuess an integer between 1 and 100: ")
        past_guesses = []
        while random_number_100 != user_guess:

            if user_guess > 100 or user_guess < 1:
                print(f"\n{Fore.RED}You can't choose {user_guess}")
                print(
                    f"{Fore.YELLOW}Pick an integer between 1-100 only!\n"
                    )
            elif user_guess > random_number_100:
                print(f"{Fore.MAGENTA}\nToo high, try a bit lower!\n")
                self.guesses += 1
                print(f"{Style.DIM}Your last guess was {user_guess}")
                past_guesses.append(user_guess)
                print(
                    f"{Style.DIM}Your previous guesses:{past_guesses}\n"
                    )
            elif user_guess < random_number_100:
                print(f"{Fore.CYAN}\nToo low, try a bit higher!\n")
                self.guesses += 1
                print(f"{Style.DIM}Your last guess was {user_guess}")
                past_guesses.append(user_guess)
                print(
                    f"{Style.DIM}Your previous guesses:{past_guesses}\n"
                    )

            user_guess = self.get_int("Guess an integer between 1 and 100: ")

        print(f"\n{Fore.GREEN}You got it! The number was: {random_number_100}")
        print(f"{Fore.GREEN}You guessed it in {self.guesses + 1} attempts!")


class ComputerGuesses(Helper):

    """
    This class represents the second game, Guess-The-Number (AI).
    The game is accessed through the play() function below.
    """

    def __init__(self):
        super().__init__()
        self.guesses = 0

    def __number_handler(self, string):
        """
        Function that handles user's chosen number for use in
        the ai guessing game
        """
        while True:
            var100 = self.get_int(string)
            if var100 >= 1 and var100 <= 100:
                return var100
            else:
                print(f"\n{Fore.RED}Input is not between 1 and 100\n")

    def __three_option_handler(self, string):
        """
        Function that handles user's chosen number for use in
        the ai guessing game
        """
        while True:
            var3 = self.get_int(string)
            if var3 >= 1 and var3 <= 3:
                break
            else:
                print(f"\n{Fore.RED}Input is not between 1 and 3\n")
        return var3

    def play(self):

        """
        A function that generates a random number guess between
        two variables of value 1 and 101, and upon user input,
        adjusts the next guess based on whether the user feedback
        requires a higher or lower number.
        """
        self.guesses = 0

        print("\nPick a number between 1 and 100, and I'll try to guess it!")
        user_number = self.__number_handler("Enter your chosen number: \n")

        mini = 1
        maxi = 101

        while True:

            try:
                computer_guess = random.randint(mini, maxi)

                print(f"\n{computer_guess}\n")
                print(f"{Style.DIM}Your number: {user_number}")
                print(
                    "Too low? Press[1]. Too high? Press[2]."
                    "Correct? press[3]\n")
                user_response = self.__three_option_handler("")
                if user_response == 1:
                    mini = computer_guess + 1
                    self.guesses += 1
                elif user_response == 2:
                    maxi = computer_guess - 1
                    self.guesses += 1
                elif user_response == 3:
                    print(
                        f"\n{Fore.GREEN}I got your number in " +
                        f"{self.guesses + 1} attempts!")
                    break

                if user_number == computer_guess:
                    print(f"\n{Fore.YELLOW}Hmmm - are you telling the truth??")
                    print(
                        f"\n{Fore.GREEN}I got your number in " +
                        f"{self.guesses + 1} attempts!")
                    break
            except ValueError:
                print(f"{Fore.RED}You're not playing the game correctly!!")
                break


class CoinToss(Helper):

    """
    This class represents the third game, Coin Toss.
    The game is accessed through the play() function below.
    """

    def __init__(self):
        super().__init__()

    def __get_toss(self, string):

        """
        Handles user input and returns the value
        """

        while True:
            user_value = self.get_int(string)
            if user_value == 0 or user_value == 1:
                return user_value
            else:
                print(f"\n{Fore.RED}Invalid input, try again\n")

    def play(self):

        """
        Function to replicate a random coin toss,
        where the user can guess in advance what the
        outcome will be.
        """
        coin = {
            "heads": 0,
            "tails": 1
        }

        input(f"\n{Fore.YELLOW}Press enter to begin...")

        coin_faces = list(coin.values())

        user_guess = self.__get_toss(
            f"{Fore.RESET}Please enter [0] for heads or [1] for tails!\n"
            )

        flip_coin = random.choice(coin_faces)
        comp_coin_value = self.get_dict_key(coin, flip_coin)
        user_coin_value = self.get_dict_key(coin, user_guess)

        while user_guess != 0 or user_guess != 1:

            try:
                if flip_coin == user_guess:
                    print(f"You guessed {user_coin_value}({user_guess})")
                    print(f"{Fore.GREEN}The result was {comp_coin_value}")
                    print("You got it!")
                    break
                elif flip_coin != user_guess:
                    print(f"You guessed {user_coin_value}({user_guess})")
                    print(f"{Fore.BLUE}The result was {comp_coin_value}")
                    print("Try again!")
                    break
            except ValueError:
                print(f"{Fore.RED}Invalid input. Enter [0] or [1] only!")
            user_guess = self.__get_toss("Enter [0] (heads) or [1] (tails)!\n")
            flip_coin = random.choice(coin_faces)
            comp_coin_value = self.get_dict_key(coin, flip_coin)
            user_coin_value = self.get_dict_key(coin, user_guess)


class Games(Helper):

    """
    This class contains handlers for running the structure of the program.
    There is a menu function that starts at the beginning of the application,
    a function to handle the user's input on which game they'd like to play
    and also a function for handling decisions at the end of a round.
    A clear-terminal function cleans up the console for the user.
    """

    def __init__(self):
        super().__init__()
        self.game1 = PlayerGuesses()
        self.game2 = ComputerGuesses()
        self.game3 = CoinToss()

    def __menu(self):
        """
        Prints the welcome message and start menu
        options and descriptions.
        """

        print(f"{Style.BRIGHT}Welcome to my Guess-The-Number application!\n")
        print("A game where you or the computer can try to guess a number.")
        print("A 'coin toss' program is included too as a bonus!\n")
        print(f"{Style.BRIGHT}Please enter:\n")
        print("0 to exit the application")
        print("1 for Guess-The-Number")
        print("2 for Guess-The-Number (AI)")
        print("3 for the 'coin-toss' program\n")

    def run(self):
        """
        Runs the menu introduction and provides player with an input to
        pick one of three options.
        """

        while True:
            self.__menu()

            menu_input = self.get_int("Please pick a number to begin: ")

            if menu_input == 0:
                break

            elif menu_input == 1:
                self.game1.play()
                self.__end_of_game(self.game1)

            elif menu_input == 2:
                self.game2.play()
                self.__end_of_game(self.game2)

            elif menu_input == 3:
                self.game3.play()
                self.__end_of_game(self.game3)
            elif menu_input > 3 or menu_input < 0:
                self.clear_terminal()
                print(f"\n{Fore.RED}Invalid option! Pick: 0, 1, 2 or 3 only\n")

                self.run()

            else:
                print("Please enter 0, 1, 2 or 3 only")
                print("0 to exit the application")
                print("1 for Guess-The-Number")
                print("2 for Guess-The-Number (AI)")
                print("3 for the 'coin-toss' program\n")

        print(f"\n{Fore.MAGENTA}Thanks for playing - Bye!\n")

    def __end_of_game(self, game):

        """
        Function to give user a choice whether to repeat the program
        or to return to the start menu.
        """

        while True:
            decision = input("\nEnter [x] - play again or [c] - go back: \n")
            if decision == "x":
                self.clear_terminal()
                game.play()
            elif decision == "c":
                self.clear_terminal()
                break
            else:
                print(f"{Fore.RED}Wrong input.\n")


Games().run()
