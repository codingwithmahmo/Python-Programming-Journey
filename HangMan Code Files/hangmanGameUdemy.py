import random
import time
#i added another library with the name of  time in this code, please review and check functionaaity
#this line is used in order to import the code from the hangman_word and hangman_art files
from hangman_words import word_list
from hangman_art import stages, logo

#this declares the lives for the user that they have
lives = 6

#prints the logo for the hangman name
print(logo)

#this randomly chooses a random word from the list that we imported
chosen_word = random.choice(word_list)
print(chosen_word)

#placeholder declared as an empty string first
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
