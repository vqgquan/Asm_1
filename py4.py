# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Vu Quoc Gia Quan (s3927120)
# Created date: 13/11/2021
# Last modified date: 18/11/2021

import turtle

# set up a graphic window
win = turtle.Screen()
win.setup(width=1000, height=1000)
win.bgcolor("white")

# create tito object from Turtle and add properties
tito = turtle.Turtle()
tito.pensize(3)
tito.shape('arrow')

# add a starting point
X = -100
Y = -100


def turtle_move(x, y):
    """
    A function to help the turtle move
    :param x:
    :param y:
    :return:
    """
    tito.up()
    tito.goto(x, y)
    tito.down()


def draw_x_and_y_axis(lengths):
    """
    Draw the x and y axis based on a given length
    :param lengths:
    :return:
    """
    turtle_move(X, Y)
    tito.seth(0)
    tito.fd(lengths)
    tito.stamp()
    turtle_move(X, Y)
    tito.left(90)
    tito.fd(lengths + 50)
    tito.stamp()


def draw_category(lengths, color_type):
    """
    Draw a bar chart for a give category and add color
    :param lengths:
    :param color_type:
    :return:
    """
    # setting a color for a category and starting to draw it
    tito.color(color_type)

    # begin filling in the color
    tito.begin_fill()

    # drawing the first vertical line
    tito.seth(90)
    tito.fd(lengths)

    # save the turtle current position to go to after finish drawing
    a, b = tito.position()

    # drawing first horizontal line
    tito.right(90)
    tito.fd(40)

    # drawing second vertical line
    tito.right(90)
    tito.fd(lengths)

    # drawing second horizontal
    tito.right(90)
    tito.fd(40)

    # finish filling in the color
    tito.end_fill()

    # reset the turtle for the next operation
    tito.color("black")
    turtle_move(a, b)


def add_date(date):
    # moving the turtle to desired position to add date
    turtle_move(-50, -100)

    # setting up the turtle for writing date information
    tito.seth(270)
    tito.up()
    tito.fd(20)

    # writing the date
    tito.write(date)


def add_total_number_of_pizza(a, b, c, d):
    """
    Add total number of pizza on top of the bar chart
    :param a:
    :param b:
    :param c:
    :param d:
    :return:
    """
    tito.write(a + b + c + d)


def draw_bar_chart(date, large_thick, large_thin, medium_thick, medium_thin):
    """
    Run the programme to draw a bar chart
    :return:
    """
    # start off with drawing both axis and add the date
    draw_x_and_y_axis(300)
    add_date(date)

    # setting up turtle and starting to draw a bar chart for each category
    turtle_move(-50, -100)
    draw_category(large_thick * 5, "aqua")
    draw_category(large_thin * 5, "aquamarine1")
    draw_category(medium_thick * 5, "aquamarine2")
    draw_category(medium_thin * 5, "aquamarine3")

    # adding total number of pizza and finishing up the bar chart
    add_total_number_of_pizza(large_thick, large_thin, medium_thick, medium_thin)
    tito.hideturtle()
    draw_x_and_y_axis(300)

    win.exitonclick()


# execute the function
draw_bar_chart('18/11/2021', 15, 12, 11, 8)
