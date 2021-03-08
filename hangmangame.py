import random
import hangman_art
import hangman_wordlist
import time
import os

# Imports the word list from < hangman_wordlist >
word_list = hangman_wordlist.word_list

# Chooses a random word in the < word_list >
chosen_word = random.choice(word_list)

# Saves the length of the chosen word
word_len = len(chosen_word)

# Defines a state to the < game_over >
game_over = False

# Defines a total of lives
lives = 6

# Displays the blanks
display = []

# Creates a function to welcome the player
def greetings():
    print(hangman_art.logo, "\nWelcome to the Hangman game. Guess the word and save the stickman!")

# Turns empty display list into a list with "_"
for i in range(word_len):
    display += "_"

# Starts the game
while game_over == False:
    greetings()                             # Calls the function < greetings() >

    print(f'{" ".join(display)}\n')         # Prints < display >
    print(hangman_art.stages[lives])        # Prints the Hangman lives
    
    guess = input("Guess a letter: ")       # Saves the user's guess
   
    if guess in display:                    # If the letter already been inserted:
        print("You aleady inserted this letter.")
        time.sleep(1.5)
    else:                                   # If not:
        for i in range(word_len):
            letter = chosen_word[i]
            if letter == guess:
                display[i] = letter

    if guess not in chosen_word:            # If the letter doesn't match in the chosen word:
        lives -= 1
        if lives == 0:                      # If the lives == 0, the user loses and the game is over
            game_over = True
            os.system("cls")
            greetings()
            print(f"{' '.join(display)}")
            print(hangman_art.stages[lives])            
            print("You lose!") 
            time.sleep(3)

    if '_' not in display:                  # If there is not more "_", the user wins and the game is over
        game_over = True
        os.system("cls")
        greetings()
        print(f"{' '.join(display)}")
        print(hangman_art.stages[lives])
        print("You win!")
        time.sleep(3)

    os.system("cls")

input()                                     # Stop condition in the end of the game