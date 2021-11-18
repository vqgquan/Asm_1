# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 13/11/2021
# Last modified date: 18/11/2021

# import functions into pycharm
import math
import random

# define z as parameter using random module
z = random.randint(100, 10000)


# define estimate_pi function
def estimate_pi(z):
    """
    calculate estimate pi by using estimate_pi function
    :param z:number of point generated made by user input
    :return:estimated_pi
    """
    # call circle_point starting at 0
    circle_point = 0

    # make a loop to calculate and count number of points inside the circle
    for i in range(1, z):
        # generate points with random coordinates
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)
        # calculate the distance_to_origin from randomly generated points
        distance_to_origin = math.sqrt(random_x ** 2 + random_y ** 2)
        # add 1 point for every generated point inside the circle
        if distance_to_origin <= 1:
            circle_point += 1

    # calculate the estimated_pi
    estimated_pi = 4 * circle_point / z

    # print out result of estimated_pi
    print("Estimated pi is: " + str(estimated_pi))

    # return estimated_pi
    return estimated_pi


# execute the function
estimate_pi(z)
