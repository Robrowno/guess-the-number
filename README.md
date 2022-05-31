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

![Responsiveness Check](/assets/readme-images/responsiveness.png)

Note: The application is run in a 'mini terminal' in the browser through Heroku. Therefore, projecting the terminal to showcase the python logic at work is more important that ensuring the width of the 'screen' is aesthetically pleasing across all devices.

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

---

## Wireframe 

- I used Blasamiq to make a flow chart to map out the logic of how I wanted the program to run. 
![Balsamiq Wireframe](/assets/readme-images/pp3-wireframe.png)

I used this model as a template for me to visualise how I was going to go about making this application.
You can see in the original flow chart I didn't come up with the option to exit the program yet. The coloured asterisks are meant to help visually guide where you are taken back to at the end of round depending on whether you want to play again or exit the game.

### Program flow charts:

- A flow chart displaying the Main Menu
### Main Menu Flow chart 
![Main Menu](/assets/readme-images/game-menu-flowchart.png)

- Game 1: Guess-The-Number
### 1st Game Flow chart 
![Game1](/assets/readme-images/game1-flowchart.png)

- Game 2: Guess-The-Number (AI)
### 2nd Game Flow chart
![Game2](/assets/readme-images/game2-flowchart.png)

- Game 3: Coin Toss
### 3rd Game Flow chart
![Game3](/assets/readme-images/game3-flowchart.png)

---

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


### User Stories

- Target Audience: A user who will want to play a command-line interface game, who will take inspiration from this to make their own Python-based game or just casually try out a new type of simple game. 

- The user can expect the following:
  - An completely intuitive game with easy to comprehend instructions/rules
  - A completely command-line-interface based game
  - No time limits. This game is to be enjoyed at the user's own pace.
  - Playable across all devices.
  - Enjoy a random-number-based game
  - Be able to exit the application at the end of a game.

---

## Technologies and Libraries Used

- Python: A form of O.O.P (Object Oriented Programming) that is used for data handling. This has been the main tool used in my project.
- Github: The cloud based service for hosting repositories for over 73 million developers.
- Gitpod: An open-source developer platform for remote development.
- Git: Used to add, commit and push my changes to the server.
- Balsamiq: Used to plan and create my wireframes for my projects.
- Heroku: Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- LucidCharts for mapping out flow charts.
- Built-in Libraries used include os and random - used for dealing with random numbers and clearing the terminal.
- Other Libraries used include Colorama - used for adding colour and style to the terminal. I specifically imported Fore and Style from Colorama to change font colours and brighten/dim text.
- PEP8 Validator for checking that my Python code meets PEP8 standards.

---

## Application Features

This application comprises of 3 core programs:

1. A guessing game (Player)
2. Another guessing game (Computer)
3. A 'Coin-Toss' program

At the beginning of the application, there is a welcome message/main menu that also re-prints at the end of a game round should the player wish to go back to the main menu:

![Welcome/Menu](/assets/readme-images/game-menu.png)

First game Option: Guess-The-Number. The player will be greeted with the start of the game like this:

![Game1 start](/assets/readme-images/game1-start.png)





### Error/Invalid input messages:




---

## Other Features to Implement

- On stack overflow, I saw a fantastic function that someone had written where they call how many times heads or tails is called out of 10,000 coin flips. I thought this was a fantastic idea and great bit of code that I would definitely want to have included in some way in the application in future. 
- I would certainly like to work with different API's to see what further functionality/interactivity I could add to the application - I would try to make more random-event based games this way.

---

## Testing and Validation

I ran my code through a PEP8 Validator and it passed with no issues/warnings:
[PEP8 Validator](http://pep8online.com)
![PEP8-check](/assets/readme-images/pep8-validation.png)


To test my application, I used of course did my preliminary checks as I went along in the terminal in Gitpod.
I did further testing in the browser on Mac through a deployed link through Heroku. 

I have also run the program on mobile. Aside from aesthetics in the 'terminal view port' width and layout, I'm happy to say the project is running well across different media. 



---

## Bugs and Issues

- Terminal Clearing: I had an issue with getting my terminal clear function to work the way I expected it to. Orginally, I inserted the clear terminal at the end of each game, however, in restructuring my run.py file, I called the clear terminal function outside of the while loop in the run function in the class Games (**line 299**) and it seemed to work at first but wouldn't work on the deployed game. I then moved the the call to the clear terminal function into the end of game function and that seemed to solve the issue!
![Clear Terminal Code](/assets/readme-images/clear-terminal-code.png)
![Clear Terminal Fix](/assets/readme-images/clear-terminal-fix.png)

- Converting back to key name from value: this was a real challenge. It was only through a source on stack overflow and some help from my friend Nickolay that we worked out how to convert values back into key-names taken from a dictionary. This solution was utilised in Game 3 (Coin Toss).
- Guessing game ai input handling issues: In the second game (Guess-The-Number (AI)), I had an issue where where you could input any integer you wanted when the "Press 1 for too low, 2 for too high or 3 for correct" Promt came up, as I used my get_int function which took any integers and returned them. I found that the way around this would be to create a function to handle this specific request - I called it three_option_handler and it only returned if the response was either 1, 2 or 3. This resolved the issue perfectly. 
- Printing a list of past guesses: Originally, I kept getting either an empty list printing to the terminal or having it display as "None". The solution was to move the empty list above the while loop in the first game as it seems that the list kept resetting as the game was running. 

---

## Peer Reviews

To get some peer reviews for this project, I went to the following:



---

## Deployment

Follow the steps below to see how to deploy a repository through Heroku:



---

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
- Responsiveness Check: [Am I Responsive?](https://ui.dev/amiresponsive)
- Flow Chart maker: [LucidChart](https://www.lucidchart.com/pages/landing/flowchart-software?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_us+tier1_desktop_search_strategic_exact_&km_CPC_CampaignId=14965870688&km_CPC_AdGroupID=137102774068&km_CPC_Keyword=flowchart%20maker&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=553386940278&km_CPC_TargetID=kwd-11327061&km_CPC_Country=1007246&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQjw1tGUBhDXARIsAIJx01mTxHtq7xGFYKWafXDEHdg5lrWjdvIRNSLoEbttCEVQMz3DcstJi3YaAmRnEALw_wcB)


I couldn't have done this project without the help of some key individuals:

- **Daisy McGirr** - My Code Institute mentor. Helped guide my along the course with advice on scope and assesment criteria, as well as ideas for the project.
- **Nickolay Ninov** - A massive thanks to Nickolay for providing so much help and support over the course of the project. He helped me resolve bugs and issues that I'd have been stuck on without his help!
- **London C.I Community** - Providing encouragement and feedback for my project which is always welcome. They continue to support as per my previous projects and are a great group to be a part of!

---

**[Return to top](#guess-the-number)**