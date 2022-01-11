#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 10, 2022
# This program asks the user to enter a whole number
# and then uses a loop to calculate and display the square
# of all numbers from 0 to the number the user entered.

def main():
    # initialize the loop counter and the power of two
    loop_counter = 0
    power_of_two = 0

    # get the user_number as a string
    user_number_string = input("Enter a whole number: ")
    print("")

    # checks to catch errors
    try:
        # change user number as string to an integer
        user_number = int(user_number_string)
        # checks to see if user number is a whole number
        if (user_number >= 0):
            # calculate the square of all numbers from 0 to user number
            for loop_counter in range(user_number + 1):
                power_of_two = loop_counter**2
                print("{}^2 ={}".format(loop_counter, power_of_two))
        else:
            print("{} is not a whole number".format(user_number_string))
    except Exception:
        print("{} is not a number.".format(user_number_string))
    finally:
        print("")
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
