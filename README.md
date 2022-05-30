# GUESS-THE-NUMBER!

Guess-The-Number is a Python based application fully run within the terminal. 

This app runs 3 core programs:
1. Guess-The-Number: The Player has to guess a randomly generated number.
2. Guess-The-Number (AI): Same as above, except this time, the computer has to try to guess the player's number!
3. Coin-Toss: A bonus program that simulates 'flipping a coin' with the computer. 

This application explores the posibilites of automation with Python, handling user inputs and random 
outcomes through the use of functions. 

The desired goals from the perspective of myself and for the player reflects this. I want to demonstrate what can be done with Python through the aim of creating 3 programs that can simulate random game events that the user is likely to have played in real life, whether attempting to guess a number that their friend was thinking of to flipping a coin to decide on who goes first in a game.

Guess-The-Number is deployed on Heroku. 

Live Link to the app on Heroku here: [Guess-The-Number](https://guess-the-number-pp3.herokuapp.com/)

---
## Application across difference platforms 


---


## Table of Contents
1. [Wireframe](#wireframe)
2. [UX Description](#ux-description)
3. [Technologies used](#technologies-used)
4. [Application Features](#application-features)
5. [Features to implement](#other-features-to-implement)
6. [Testing and Validation](#testing-and-validation)
7. [Bugs and Issues](#bugs-and-issues)
8. [Peer Reviews](#peer-reviews)
9. [Deployment](#deployment)
10. [Credits](#credits)

## Wireframe 

- I used Blasamiq to make a flow chart to map out the logic of how I wanted the program to run. 
![Balsamiq Wireframe](/assets/readme-images/pp3-wireframe.png)

I used this model as a template for me to visualise how I was going to go about making this application.
You can see in the original flow chart I didn't come up with the option to exit the program yet. The coloured asterisks are meant to help visually guide where you are taken back to at the end of round depending on whether you want to play again or exit the game.

### Program flow charts:

### Main Menu Flow chart 
![Main Menu](/assets/readme-images/game-menu-flowchart.png)

### 1st Game Flow chart 
![Game1](/assets/readme-images/game1-flowchart.png)

### 2nd Game Flow chart
![Game2](/assets/readme-images/game2-flowchart.png)

### 3rd Game Flow chart
![Game3](/assets/readme-images/game3-flowchart.png)


## UX Description

### How to play the game:

Guess-The-Number is an input based application, where depending on assigned input options, the player can make guesses or make selections on what game they'd like to play. 

In the first game, Guess-The-Number, the player must try to guess a number between 1-100, which the computer has "thought off".
The player can enter a number one at a time, and they will get feedback from the terminal on whether their guess was higher or lower than the computer's number. When they guess correctly, they will be told along with the number of attempts it took to guess it.

A prompt then encourages the player to either play again, or, go back to the main menu. 

In the second game, Guess-The-Number (AI), the player now calls the number they're thinking of between 1-100. 
The computer makes guesses and the player provides feedback on whether the guess is too low, high or spot on. 
This is done by entering 1 for too low, 2 for too high and 3 for a correct guess.
The computer then prints how many attempts it took to guess the player's number.

A prompt then encourages the player to either play again, or, go back to the main menu.

In the third and final game, Coin-Toss, the player hits enter to begin and is asked to call Heads or Tails
by selecting 0 or 1 on their keyboard respectively. 

The computer will "flip a coin" and the result of the coin toss is printed.
Whilst this is predominantly a player vs computer coin toss, you could use this program to make a traditional coin toss decision as well!

As per the previous games, a prompt then encourages the player to either play again, or, go back to the main menu.

## Technologies Used

- Python: A form of O.O.P (Object Oriented Programming) that is used for data handling. This has been the main tool used in my project.
- Github: The cloud based service for hosting repositories for over 73 million developers.
- Gitpod: An open-source developer platform for remote development.
- Git: Used to add, commit and push my changes to the server.
- Balsamiq: Used to plan and create my wireframes for my projects.
- Heroku: Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

## Application Features

This application comprises of 3 core programs:

1. A guessing game (Player)
2. Another guessing game (Computer)
3. A 'Coin-Toss' program

At the beginning of the application, there is a welcome message/main menu that also re-prints at the end of a game round should the player wish to go back to the main menu.



## Other Features to Implement

- On stack overflow, I saw a fantastic function that someone had written where they call how many times heads or tails is called out of 10,000 coin flips. I thought this was a fantastic idea and great bit of code that I would definitely want to have included in some way in the application in future. 

## Testing and Validation

## Bugs and Issues

- Terminal Clearing
- Converting back to key name from value
- Guessing game ai input handling issues


## Peer Reviews

## Deployment

## Credits

I sought inspiration from many different websites/sources for this project. 
With many thanks to the following:

- An example guessing game by PythonForBeginners: [PythonForBeginners Link_1](https://www.pythonforbeginners.com/code-snippets-source-code/python-guessing-game)
- An example coin-toss game that returns the result of 10,000 coin tosses: [PythonForBeginners Link_2](https://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python)
- Lessons on a 2 guessing games inspired this project from freeCodeCamp.org: [freeCodeCamp](https://www.youtube.com/watch?v=8ext9G7xspg&list=WL&index=1)
- Superb information on handling user inputs: [TowardsDataScience](https://towardsdatascience.com/a-complete-guide-to-user-input-in-python-727561fc16e1#:~:text=Python%20provides%20a%20simple%20framework%20for%20getting%20user%20input.,input%20into%20the%20required%20format.)
- "Key by Value" solution for my coin toss game inspired by this answer on Stack Overflow: [Stack Overflow Link_1](https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary)
- Solution for finding a way to clear the terminal as a function from Stack Overflow: [Stack Overflow Link_2](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
- Colorama Youtube tutorial by Tech with Tim: [Tech With Tim](https://www.youtube.com/watch?v=u51Zjlnui4Y)
- Link to Colorama page/tutorial: [Colorama](https://pypi.org/project/colorama/)


I couldn't have done this project without the help of some key individuals:

- Daisy McGirr - My Code Institute mentor. Helped guide my along the course with advice on scope and assesment criteria, as well as ideas for the project.
- Nickolay Ninov - A massive thanks to Nickolay for providing so much help and support over the course of the project. He helped me resolve bugs and issues that I'd have been stuck on without his help!
- London C.I Community - Providing encouragement and feedback for my project which is always welcome. They continue to support as per my previous projects and are a great group to be a part of!