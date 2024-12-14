"""
Turtle Race
"""
import turtle
import random
from PIL import Image

# ================= Instructions at the bottom of this file ===================


def screen_clicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))


def draw_background():
    filename = 'race_track.gif'

    try:
        image = Image.open(filename)
    except(FileNotFoundError, IOError):
        print("ERROR: Unable to find file " + filename)
        return

    window = turtle.Screen()
    window.setup(image.width + 100, image.height + 100, startx=0, starty=0)
    window.bgpic(filename)
    window.onclick(screen_clicked)

# ====================== DO NOT EDIT THE CODE ABOVE ===========================


if __name__ == '__main__':
    draw_background()

    # TODO 1) Create an empty list of turtles

    william_beckwith = turtle.Turtle()
    ur_dad_left_for_da_milk = turtle.Turtle()
    sparsh_thakore = turtle.Turtle()
    matteeshee = turtle.Turtle()

    # TODO 2) Create a new turtle and set its shape to 'turtle
    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle = turtle.Turtle()
    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle.shape('turtle')

    # TODO 3) Set the turtle's speed to 3
    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle.speed(3)
    # TODO 4) Set the turtle's pen up
    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle.penup()
    # TODO 5) Use the turtle's goto() method to set its position on the left
    #  side of the screen
    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle.goto(-400, 200)
    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle.width(10)

    # TODO 6) use a loop to repeat the previous instructions and create
    #  8 turtles lined up on the left side of the screen
    #  *HINT* click on the window to print the corresponding x, y location
    william_beckwith.speed(10)
    william_beckwith.penup()
    william_beckwith.goto(-400, 140)
    william_beckwith.shape('turtle')

    ur_dad_left_for_da_milk.speed(3)
    ur_dad_left_for_da_milk.penup()
    ur_dad_left_for_da_milk.goto(-400, 78)
    ur_dad_left_for_da_milk.shape('turtle')

    sparsh_thakore.speed(10)
    sparsh_thakore.penup()
    sparsh_thakore.goto(-400, 27.5)
    sparsh_thakore.shape('turtle')

    matteeshee.speed(10)
    matteeshee.penup()
    matteeshee.goto(-400, -141)
    matteeshee.shape('turtle')
    matteeshee.shapesize(19)
    # TODO 7) Move each turtle forward a random distance between 1 and 20
    distance = random.randint(1, 20)
    distance2 = random.randint(1, 20)
    distance3 = random.randint(1, 20)
    distance4 = random.randint(1, 20)
    distance5 = random.randint(1, 20)

    Pneumonoultramicroscopicsilicovolcanoconiosis_turtle.forward(distance)
    william_beckwith.forward(distance2)
    ur_dad_left_for_da_milk.forward(distance3)
    sparsh_thakore.forward(distance4)
    matteeshee.forward(distance5)
    # TODO 8) Create a loop to keep moving each turtle until a turtle
    #  crosses the finish line
    #  *HINT* click on the window to print the corresponding x, y location
    for i in range(50):

    # TODO 9) When a turtle crosses the finish line, stop the race and
    #  indicate which turtle won the race.

    # EXTRA: Create different colors for each turtle and code a special
    # dance for the winning turtle!

    turtle.done()
