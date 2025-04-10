# -*- coding: utf-8 -*-
"""password_generator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14XGtCTEze10eTmwUlbPjOIZ8UQ1e9-Sl
"""



"""A Password Generator is a useful Python project that creates strong, random passwords for users. The passwords are generated with a combination of letters, numbers, and special characters, making them secure and difficult to guess."""

import random
import string

# Function to generate a random password
def generate_password(length=12, use_special_chars=True, use_numbers=True, use_uppercase=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build the pool of characters based on user preferences
    char_pool = lowercase  # Start with lowercase letters

    if use_uppercase:
        char_pool += uppercase
    if use_numbers:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Generate a random password
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

# Function to get user input
def get_user_input():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 8:
                print("Password length should be at least 8 characters for better security.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the password length.")

    # Ask if user wants to include special characters, numbers, and uppercase letters
    use_special_chars = input("Include special characters? (yes/no): ").lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
    use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"

    return length, use_special_chars, use_numbers, use_uppercase

# Main function to run the password generator
def main():
    print("Welcome to the Password Generator!")

    # Get user input for password preferences
    length, use_special_chars, use_numbers, use_uppercase = get_user_input()

    # Generate the password based on the input
    password = generate_password(length, use_special_chars, use_numbers, use_uppercase)

    # Display the generated password
    print(f"Generated password: {password}")

# Run the program
main()