# Final-Project
I first establish a player class. Which initializes a player with a name and sets counters for letter and word guesses to zero. The correct flag indicates whether the player has correctly guessed the word.
Next, I put a chosen_word function which serves to randomly select a word from the provided word bank.
This underline_letter function works with the display_status function, it helps create another display space for the correctly guessed letters.
Next, is the display_status function which shows the current status of the secret word with the correctly guessed letters in 1 line and all the guessed letters including the wrong ones in the next line. They are both clearly labelled.
After that, I created my player_turn function, which manages a single player's turn. It displays the current word status, prompts the player to guess a letter, updating the letter guesses count and the list of guessed letters, checks if the letter is in the secret word and informs the player and also gives the player the option to guess the entire word.
The clear_screen function that follows just clears the terminal screen so that only my game can be seen while playing it. And it starts off as soon as the game file is run.
I then have my main game function, which manages the overall flow of the game. It starts with a welcome message and then prompts for the number of players and their names, which results in creating player objects.
I added 2 additional word banks this time, giving the players more options to choose from, to guess words from. The function prompts them to choose one of the three options and then selects a random word from the word bank that the players choose.
The code then selects a random secret word and starts the game loop. Wherein it continuously cycles through players, allowing each player to take a turn until a player guesses the word or exceeds the maximum word guesses.
I then added a pandas function that serves to store and collect player statistics in a DataFrame and print the final statistics.
Finally, is the game_over function which checks if the game is over based on players' actions and if so displays an end message that says which player won with how many letter guesses and word guesses.
