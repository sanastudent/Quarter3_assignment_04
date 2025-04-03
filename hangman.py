# -*- coding: utf-8 -*-
"""Hangman.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bnSbAv54uzf3EZd4HcRmORyo7ICKmtB8
"""



""" Project 5: Hangman Game using Python. Hangman is a classic word-guessing game where the player tries to guess a hidden word by suggesting letters within a certain number of attempts. The game continues until the player either guesses the word correctly or runs out of attempts."""

import random

# List of words to guess
word_list = ["python", "hangman", "developer", "computer", "programming", "challenge", "algorithm"]

# Function to display the current state of the word (with guessed letters)
def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

# Function to display hangman state
def display_hangman(incorrect_guesses):
    hangman_states = [
        '''
           -----
           |   |
               |
               |
               |
               |
        -----------''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        -----------''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        -----------''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        -----------''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        -----------''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        -----------''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        -----------'''
    ]
    print(hangman_states[len(incorrect_guesses)])

# Main Hangman Game Function
def hangman():
    word_to_guess = random.choice(word_list)  # Randomly pick a word
    guessed_letters = []  # Track the player's guessed letters
    incorrect_guesses = []  # Track incorrect guesses
    attempts_left = 6  # The player has 6 attempts before the game ends

    print("Welcome to Hangman!")

    while attempts_left > 0:
        # Display current word with blanks and guessed letters
        print("\nCurrent word: ", display_word(word_to_guess, guessed_letters))

        # Display incorrect guesses
        print("Incorrect guesses: ", " ".join(incorrect_guesses))

        # Display remaining attempts
        print(f"Attempts remaining: {attempts_left}")

        # Ask the user for a letter
        guess = input("Guess a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        # Check if the letter has been guessed before
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You've already guessed that letter. Try again.")
            continue

        # If the guess is correct
        if guess in word_to_guess:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.append(guess)
            attempts_left -= 1
            display_hangman(incorrect_guesses)
            print(f"Sorry, '{guess}' is not in the word.")

        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word_to_guess):
            print("\nCongratulations! You've guessed the word correctly!")
            break

    if attempts_left == 0:
        print("\nSorry, you've run out of attempts. The word was:", word_to_guess)

# Run the Hangman Game
hangman()