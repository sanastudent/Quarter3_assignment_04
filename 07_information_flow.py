# -*- coding: utf-8 -*-
"""07_information_flow.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Y2lhSHJpUl-CDrBhPawbe7b_J475z-Xt
"""

# 01
# There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!
# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to
#  ADULT_AGE.
# If the function takes an age less than ADULT_AGE, return False instead.

ADULT_AGE : int  = 18

def is_adult(age:int):
    if age >= ADULT_AGE:
        return True

    return False

def main():
    age : str = int(input("How old is this person?"))
    print(is_adult(age))

# 02
# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting.
#  Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

def main_two():
    name : str = input("What's your name?")
    print(greet(name))


def greet(name):
    return f"Greetings {name}!"


# 03
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

def in_range(n,low,high):

    if n >= low and n <= high:
        return True

    return False

result = in_range(5,1,10)
print(result)


# 04
# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit
#  are in her inventory. Write code in main() which will:
#
# Prompt the user to enter a fruit ("Enter a fruit: ")
#
# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock
#
# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)
#
# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

def num_in_stock(fruit):
    inventory = {
        "apple": 10,
        "banana" : 25,
        "orange" : 30,
        "grapes" : 35
    }

    return inventory.get(fruit.lower(), 0)

def fruit():
    fruit = input("Enter a fruit:").strip()
    stock_count = num_in_stock(fruit)

    if stock_count > 0:
        print(f"There are {stock_count} {fruit}s in stock.")

    else:
        print("This fruit is not in stock.")

# 04
# There are times where you are working with lots of different data within a function that you want to return.
#  While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.
# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:
#
# Asks the user for their first name and stores it in a variable
#
# Asks the user for their last name and stores it in a variable
#
# Asks the user for their email address and stores it in a variable
#
# Returns all three of these pieces of data in the order it was asked
#
# You can return multiple pieces of data by separating each piece with a comma in the return line.

def get_user_info():
    first_name : str = input("What is your first name?")
    last_name : str = input("What is your last name?")
    email_address : str = input("What is your email address?")

    return first_name,last_name,email_address

def user():
    user_data = get_user_info()
    print("Received the following user data:", user_data)


# 05
# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function!
# if you're stuck revisit the add_five example from lecture.

def main_three():
    num : int = 7
    num = subtract_seven(num)
    print("This should be zero:", num)

def subtract_seven(num):
    num = num - 7
    return num






if __name__ == '__main__':
    main()
    main_two()
    fruit()
    user()
    main_three()