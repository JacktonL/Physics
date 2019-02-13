from graphics import GraphWin, Rectangle, Point
from time import sleep

size = 500

win = GraphWin("Gravity", size, size)

rect = Rectangle(Point(size/2-25, 0), Point(size/2+25, 50))
rect.setFill("red")

rect.draw(win)

g = -9.0665/100

v = 0

c = 0

u = 0


while True:

    bottom = size - rect.getP2().getY()

    rect.move(0, -v)

    v = u + g*c
    print(v)

    bottom += v

    c += 1

    if bottom <= 0:
        u = -v
        c = 0

    sleep(0.01)

