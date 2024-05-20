import os
import random
import pandas as pd



class Player:
    def __init__(self, name):
        self.name = name
        self.letter_guesses = 0
        self.word_guesses = 0
        self.correct = False

def chosen_word(word_bank): 
    return random.choice(word_bank)

def underline_letter(letter):
    return f"{letter}"

def display_status(secret_word, guessed_letters):
    display_word = ''.join([underline_letter(letter) if letter in guessed_letters else '' for letter in secret_word])
    print("Correct letters: ", ' '.join(display_word))
    print("Guessed letters: ", ', '.join(guessed_letters))

def player_turn(player, secret_word, guessed_letters):
    print(f"{player.name}'s turn.")
    display_status(secret_word, guessed_letters)
    
    letter = input("Guess a letter: ").lower()
    player.letter_guesses += 1

    if letter in secret_word:
        print(f"There are {secret_word.count(letter)} '{letter}'s in the word.")
    else:
        print(f"There are no '{letter}'s in the word.")
    guessed_letters.append(letter)

    guess_word = input("Do you want to guess the word? (yes/no): ").lower()
    if guess_word == 'yes':
        word_guess = input("Enter your word guess: ").lower()
        player.word_guesses += 1
        if word_guess == secret_word:
            print(f"Congratulations, {player.name}! You guessed the word correctly and are the WINNER!")
            player.correct = True
        else:
            print("Incorrect guess.")
    print()

def clear_screen():
    # Clear the terminal screen based on the operating system
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def game():
    clear_screen()
    print("Welcome to Abhi's Word Guessing Game!")
    print("You are going to be guessing different WORDS")

    num_players = int(input("Enter the number of players: "))
    players = [Player(input(f"Enter the name of player {i+1}: ")) for i in range(num_players)]

    # List of secret words
    available_word_bank = input("Which word bank would you like to use? Sports, animals or coding languages: ").lower()
    if available_word_bank == "sports":
        word_bank = ["basketball", "football", "soccer", "tennis", "badminton", "swimming", "golf", "cricket", "lacrosse", 'wrestling']
    if available_word_bank == "animals":
        word_bank = ["chicken", "lion", "tiger", "elephant", "camel", "wolf", "cow", "horse", "dog", "cat", "snake"]
    if available_word_bank == "coding languages":
        word_bank = ["python", "java", "kotlin", "swift", "ocaml", "c++"]

    secret_word = chosen_word(word_bank)
    guessed_letters = []

    game_over = False
    while not game_over:
        for player in players:
            if player.correct:
                continue
            player_turn(player, secret_word, guessed_letters)
            if player.correct:
                game_over = True
            elif player.word_guesses >= 3:
                game_over = True
                print(f"{player.name} you have lost as you guessed incorrectly 3 times!")
                break

# Create a DataFrame to store and display player statistics
    data = {
        'Player': [player.name for player in players],
        'Letter Guesses': [player.letter_guesses for player in players],
        'Word Guesses': [player.word_guesses for player in players],
        'Correct': [player.correct for player in players]
    }
    df = pd.DataFrame(data)
    df['Status'] = df['Correct'].apply(lambda x: 'Winner' if x else 'Lost')

    print("\nGame over!")
    for player in players:
        if player.correct:
            print(f"{player.name} wins with {player.letter_guesses} letter guesses and {player.word_guesses} word guesses!")
            print(df[['Player', 'Letter Guesses', 'Word Guesses', 'Status']])
        else:
            continue

if __name__ == "__main__":
    game()