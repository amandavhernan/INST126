# Project 1: Building a Calculator
This is my first project for INST126 at the University of Maryland. For this project, I converted a flowchart that contained all of the major steps to create basic calculator into a working python program. 
I decided to take it a bit further and added more functionality to my calculator. In addition to the basic operations (addition, subtraction, multiplication, and division), my calculator can also take the square root of any number, raise any number to the power of 2 or 3, and take the natural logarithm of any number. I also added a loop, which allows the user to continue entering operations until they type "quit".

## How it works
When the user runs this program, it will ask the user to choose an operation by using the menu provided. Make sure to enter the numerical label given to each operation. 
For example, if the user wants to choose "Add", they must enter "1". If the user wanted "Square Root, they must enter "5" and so on. If the user does not enter a valid number/operation (1-8), the program will not run and the user will see an error. 
The error prompts the user to try again by entering a number between 1 through 8. If the user wants to stop the program, they must enter "quit" when prompted for an operation. 

# Project 2: Hangman
This is my second project for INST126 at the University of Maryland. For this project, I created a flowchart that represented how my game would work. Then, I had to figure out the decryption mechanism and implement that into the program so the encrypted words would be decrypted once the user correctly guessed all of the letters. 

## How it works
When the user runs this program, it will randomly choose a word from a preselected list of encrypted words for the user to guess. Then, it will ask the user to guess a letter. The user gets 10 lives or guesses, and if the user guesses a letter incorrectly, they will lose one life. If the user guesses a letter correctly, they will not lose a life and will be able to continue guessing as long as they continue to guess the letters correctly. If the user does not enter a valid letter or guesses the same letter, the program will prompt them to try again. Once the user has guessed all of the correct letters in the word, the program will show the user the decrypted version of the word. 

As the user plays the game, the program will show them how many lifes and which letters they have already guessed. The program will also show the current word with dashes that represent the letters that still need to be guessed and letters in place of the letters that were guessed correctly.

### From the user's perspective, it will look like this once the program starts: 

You have 10 lives left and you have used the following letters:  
Current word:  - - - - - -

### And once the user starts guessing letters, it will look like this: 

You have 10 lives left and you have used the following letters:  A

Current word:  A - A - - A

### If the user guesses incorrectly, it will look like this: 

Sorry, the letter you guessed is not in the word.

You have 9 lives left and you have used the following letters:  A B

Current word:  A - A - - A
