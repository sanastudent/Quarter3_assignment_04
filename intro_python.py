# -*- coding: utf-8 -*-
"""intro_python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zipN4PaYcGj5VMeNybufziwdDgqmGFtQ
"""

# 01. add_two_numbers

#Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:
#Prompt the user to enter the first number.
#Read the input and convert it to an integer.
#Prompt the user to enter the second number.
#Read the input and convert it to an integer.
#Calculate the sum of the two numbers.
#Print the total sum with an appropriate message.

def main():
    # Prompt the user to enter the first number
    first_number = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    second_number = int(input("Enter the second number: "))

    # Calculate the sum of the two numbers
    total_sum = first_number + second_number

    # Print the total sum with an appropriate message
    print("The total sum is:", total_sum)


# 02. favourite animal
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!"
# (the blank should be filled in with the user-inputted animal, of course).


def main_two():
    # Ask the user for their favorite animal
    favourite_animal = input("What is your favourite animal? ")

    # Respond with the message including their input
    print(f"My favourite animal is also {favourite_animal}!")

# 03. farenheit_to_celcius
#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!)
# and outputs the temperature converted to Celsius.

def main_three():

    farenheit = float(input("Enter temprature in farenheit: "))

    # Convert the Fahrenheit temperature to Celsius
    celsius = (farenheit - 32) * 5.0 / 9.0

    print(f"The temprature in celcius is: {celsius:.2f}°C")



# 04.
#Write a program to solve this age-related riddle!

#Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

#Anton is 21 years old.

#Beth is 6 years older than Anton.

#Chen is 20 years older than Beth.

#Drew is as old as Chen's age plus Anton's age.

#Ethan is the same age as Chen.

#Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization
 #and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct
 #values!):

#Anton is 3,Beth is 4,Chen is 5,Drew is 6,Ethan is 7
def main_four():
    Anton = 21
    Beth = Anton + 6
    Chen = Beth + 20
    Drew = Chen + Anton
    Ethen = Chen

    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethen is {Ethen}")

#05.
#Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle
#  (the sum of all of the side lengths).
#Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle
# (the sum of all of the side lengths).
##
##Here's a sample run of the program (user input is in bold italics):
##
##What is the length of side 1? 3
##
##What is the length of side 2? 4
##
##What is the length of side 3? 5.5
##
#The perimeter of the triangle is 12.5

def main_five():
    side1 : float = float(input("What is the length of side1?"))
    side2 : float = float(input("what is the length of side2?"))
    side3 : float = float(input("what is the length of side3?"))

    perimeter = side1 + side2 +side3

    print(f"The perimeter of triangle is: {perimeter}")

# 06.
#Ask the user for a number and print its square (the product of the number times itself).
#Here's a sample run of the program (user input is in bold italics):
#Type a number to see its square: 4
#4.0 squared is 16.0

def main_six():
    try:
        number : float = float(input("type a number to see its square:"))
        square  = number * number
        print(f"{number} squared is {square}")

    except ValueError:
        print("Please enter a valid number.")


# Python file to call the main() function.
if __name__ == '__main__':
    main()    # Calls the first function
    main_two() # Calls the second function
    main_three() # calls the third function
    main_four()
    main_five()
    main_six()