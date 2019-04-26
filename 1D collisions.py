from graphics import GraphWin, Rectangle, Point
from time import sleep
from random import randint

size = 500
half = size/2


def window():
    win = GraphWin("Collsions", size, size)
    return win


def start():

    m1 = input("Mass 1: ")
    m2 = input("Mass 2: ")

    return m1, m2


def rect():
    mass = start()

    m1 = int(mass[0])
    m2 = int(mass[1])

    rect1 = Rectangle(Point(50, half+m1), Point(50+m1*2, half-m1))
    rect2 = Rectangle(Point(size-50, half+m2), Point(size-m2*2-50, half-m2))

    rect1.setFill("Blue")
    rect2.setFill("Red")

    return rect1, rect2, size-100-m1*2-m2*2, m1, m2


def anim(rect1, rect2, dist, mass1, mass2):

    win = window()

    rect1.draw(win)
    rect2.draw(win)

    v1 = 3
    v2 = -3

    m1 = mass1*2
    m2 = mass2*2

    distance = dist
    left = 50
    right = size-50

    while True:

        u1 = v1
        u2 = v2

        rect1.move(v1, 0)
        rect2.move(v2, 0)
        distance -= v1-v2
        left += v1
        right += v2
        sleep(0.02)
        if distance <= 0:
            v1 = (m1-m2)/(m1+m2)*u1 + (2*m2)/(m1+m2)*u2
            v2 = (2*m1)/(m1+m2)*u1 + (m2-m1)/(m1+m2)*u2

        if left <= 0:
            v1 *= -1

        if right >= size:
            v2 *= -1


hold = rect()

anim(hold[0], hold[1], hold[2], hold[3], hold[4])
