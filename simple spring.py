from graphics import GraphWin, Rectangle, Point
from math import sin, pi, cos
from math import radians as rad
from time import sleep


size = 500
half = size/2
win = GraphWin("SPRING", size, size)

rect = Rectangle(Point(half-25, size-50), Point(half+25, size))
rect.setFill("red")
rect.draw(win)

pos = win.getMouse()
print(pos, "start")
x = pos.getX() - half


cen = rect.getCenter()

for i in range(1000):

    dist = 4*pi*sin(rad(4*pi*i))
    rect.move(dist+x, 0)

    if cen.getX() >= rect.getCenter().getX():
        print(cen.getX(), "min")
    else:
        print(cen.getX())

    cen = rect.getCenter()

    sleep(0.1)
