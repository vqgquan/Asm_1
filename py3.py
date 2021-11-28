# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 13/11/2021
# Last modified date: 24/11/2021

# Import the math function
import math


# Define flour_order function
def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    """
    Decide between provider A and B based on amount of flour needed
    :param large_thick:
    :param large_thin:
    :param medium_thick:
    :param medium_thin:
    :return:integer, string, integer
    """
    # Call and make all value to integer
    total_flour = int(flour_amount(large_thick, large_thin, medium_thick, medium_thin))
    money_on_a = int(money_spent_on_a(total_flour))
    money_on_b = int(money_spent_on_b(total_flour))
    # Print out the result of the function
    print('We need to order ' + str(total_flour) + ' kg of flour, which costs ' + str(
        money_on_a) + ' VND if we buy from A and ' + str(money_on_b) + ' VND if we buy from B.')
    # Use if statement to decide choosing A or B for flour supply
    if money_on_a <= money_on_b:
        return total_flour, "A", money_on_a
    return total_flour, "B", money_on_b


# Define a function to help round up number
def round_up_to_even(a):
    """
    help to round up to even numbers
    :param a: none
    :return: round up to even a
    """
    # Using math ceiling function and some simple math to help round up numbers to even
    return math.ceil(a / 2.) * 2


# Define flour_amount function
def flour_amount(large_thick, large_thin, medium_thick, medium_thin):
    """
    Calculate the actual amount of flour needed
    :param large_thick:
    :param large_thin:
    :param medium_thick:
    :param medium_thin:
    :return: integer
    """
    # Calculate the actual amount of flour needed to make the pizzas
    flour_needed = (large_thick * 0.55 + large_thin * 0.5 + medium_thick * 0.45 + medium_thin * 0.4) * 106 / 100
    # Round up to even the amount of flour needed
    actual_amount_of_flour = round_up_to_even(flour_needed)
    return actual_amount_of_flour


# Define money_spent_on_a function
def money_spent_on_a(actual_amount_of_flour):
    """
    Calculate the amount of money needed to when buying from A
    :param actual_amount_of_flour:
    :return: integer
    """
    money_a = actual_amount_of_flour * 30000
    # Using if statement to calculate the money needed and minus the discount from A
    if actual_amount_of_flour < 30:
        money_a -= money_a * 0.03
    else:
        money_a -= money_a * 0.05
    return money_a


# define money_spent_on_b function
def money_spent_on_b(actual_amount_of_flour):
    """
    Calculate the amount of money needed to when buying from B
    :param actual_amount_of_flour:
    :return: integer
    """
    money_b = actual_amount_of_flour * 31000
    # Using if statement to calculate the money needed and minus the discount from B
    if actual_amount_of_flour < 40:
        money_b -= money_b * 0.05
    else:
        money_b -= money_b * 0.1
    return money_b


# Execute function
flour_order(10, 30, 10, 50)
