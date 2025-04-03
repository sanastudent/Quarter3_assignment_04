# -*- coding: utf-8 -*-
"""03_if_statement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IcUTGQkTIVwxBKG8jeiy2Ikd_7IX0Dgn
"""

import random


# 01.
# write a program that prints the first 20 even numbers. There are several correct approaches , but they all use a loop of some sort.Do not
# write twenty print statements.

def main():
    # Pehle 20 even numbers print karna
     for i in range(20):
          print( i * 2)




# 02.
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 45


def main2():
     user_age  = int(input("How old are you?"))

     if user_age >= PETURKSBOUIPO_AGE:
          print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}")
     else:
          print(f"You cannot vote in Peturksbouipo  where the voting age is {PETURKSBOUIPO_AGE}")

          # check if user can vote in stanlau
     if user_age >= STANLAU_AGE:
          print(f"You can vote in stanlau where the voting age is {STANLAU_AGE}")
     else:
          print(f"You can not vote in Satnlau where the voting ige is {STANLAU_AGE}")

     if user_age >= MAYENGUA_AGE:
          print(f"you can vote in Mayengua where the voting age is {MAYENGUA_AGE}")

     else:
          print(f"You can not vote in Mayengua where the voting age is {MAYENGUA_AGE}")


# 03 .
# Write a program that reads a year from the user and tells whether a given year is leap year or not.

def leap_year():
     year = int(input("Please input a year"))

     if year % 4 == 0:
          if year % 100 == 0:
               if year % 400 == 0:
                    print("That's leap year! ")
               else: # not ivisible by 400
                    print("That's not leap year!")
          else: # not divisible by 100
               print("That's a leap year")
     else: # not divisible by 4
          print("That's not a leap year")


# 04.
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

MINIMUM_HEIGHT : int = 50 # arbitrary units
def height():
     height = float(input("How tall are you?"))
     if height >= MINIMUM_HEIGHT:
          print("you're tall enough to ride!")
     else:
          print("You're not tall enough to ride!")


# 05.
# Print 10 random numbers in the range 1 to 100.

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE :int = 100

def random_value():
     for _ in range(N_NUMBERS):
          print(random.randint(MIN_VALUE,MAX_VALUE), end =" ")



if __name__ == '__main__':
    main()
    main2()
    leap_year()
    height()
    random_value()