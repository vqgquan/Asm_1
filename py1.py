# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 12/11/2021
# Last modified date: 18/11/2021

import random


def find_split_80(integer_list):
    """
    find the number in the given 20 integer list where exactly 80% of numbers in the list are equal to or smaller than it (not including itself).
    :param integer_list: list of integer generated randomly
    :return: split_80
    """

    # sort the input for integer list
    integer_list.sort()

    # choose the correct number
    split_80 = integer_list[16]

    # return the desire number
    return split_80


def random_integer_list(n):
    """
    generate a random integer list for test cases
    :param n: length of the list
    :return:
    """
    # Define an integer_list
    integer_list = []
    # make a loop to generate amount of numbers based on n
    for i in range(n):
        integer_list.append(random.randint(0, 100))
    return integer_list


# execute the function
integer_list = random_integer_list(20)
print(integer_list)
print(find_split_80(integer_list))
