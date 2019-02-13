from graphics import GraphWin, Circle, Point
from time import sleep
import random


class Window:

    def __init__(self):

        self.size = 500

    def graph(self):

        win = GraphWin("Collisions", self.size, self.size)
        return win


class Circles(Window):

    def __init__(self):

        Window.__init__(self)
        self.vx = 0
        self.vy = 0
        self.m = 0
        self.px = 0
        self.py = 0
        self.circle = Circle(Point(self.px, self.py), self.m)
        self.xcord = self.circle.getCenter().getX()
        self.ycord = self.circle.getCenter().getY()

    def define(self, num):
        m = input("Mass {}:".format(num))
        self.m = int(m)

    def getTop(self):
        top = self.ycord - self.m
        return top

    def getBottom(self):
        bottom = self.size - self.ycord + self.m
        return bottom

    def getRight(self):
        right = self.size - self.xcord + self.m
        return right

    def getLeft(self):
        left = self.xcord - self.m
        return left
