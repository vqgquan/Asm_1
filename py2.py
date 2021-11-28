# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 13/11/2021
# Last modified date: 24/11/2021

# import functions into pycharm
import math
import random

# define z as parameter using random module
z = random.randint(100, 10000)


# define generate_random_point function
def generate_random_point(z):
    """
    Generate selected number of points
    :param z: number of point
    :return:circle_points
    """
    # add the circle_point starting from 0
    circle_points = 0
    # make a loop to calculate and count number of points inside the circle
    for i in range(1, z):
        # generate points with random coordinates
        random_x = random.uniform(-1, 1)
        random_y = random.uniform(-1, 1)
        # add a conditional statement to increase number of points inside the circle using distance_to_origin function
        if distance_to_origin(random_x, random_y):
            circle_points += 1
    return circle_points


# define distance_to_origin function
def distance_to_origin(x, y):
    """
    calculate distant from each point to original point
    :param x: x coordinate of random points
    :param y: y coordinate of random points
    :return: Boolean
    """
    # calculate the distant to original point
    distance_to_origin = math.sqrt(x ** 2 + y ** 2)
    for i in range(1, z):
        # add a conditional statement and return a Boolean value when the condition is met
        if distance_to_origin >= 1:
            return False
        return True


# define estimate_pi function
def estimate_pi(z):
    """
    calculate estimate pi by using estimate_pi function
    :param z:number of point generated made by user input
    :return:estimated_pi
    """
    inside_circle_points = generate_random_point(z)
    # calculate the estimated_pi
    estimated_pi = 4 * inside_circle_points / z
    # print out result of estimated_pi
    print("Estimated pi is: " + str(estimated_pi))
    # return estimated_pi
    return estimated_pi


# execute the function
estimate_pi(z)
