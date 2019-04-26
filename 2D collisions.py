from graphics import GraphWin, Rectangle, Point
from time import sleep
import random


class Collisions:

    neg_list = [1, -1]
    rand_list = range(5, 8)

    def __init__(self):

        self.size = 500
        self.v1x = Collisions.neg_list[random.randint(0, 1)]*Collisions.rand_list[random.randint(0, 2)]*random.random()
        self.v1y = Collisions.neg_list[random.randint(0, 1)]*Collisions.rand_list[random.randint(0, 2)]*random.random()
        self.v2x = Collisions.neg_list[random.randint(0, 1)]*Collisions.rand_list[random.randint(0, 2)]*random.random()
        self.v2y = Collisions.neg_list[random.randint(0, 1)]*Collisions.rand_list[random.randint(0, 2)]*random.random()
        # self.v1x = 3
        # self.v1y = 3
        # self.v2x = -3
        # self.v2y = -3
        self.m1 = 0
        self.m2 = 0

    def window(self):

        win = GraphWin("2D Collisions", self.size, self.size)

        return win

    def define(self):

        m1 = int(input("Mass 1: "))
        m2 = int(input("Mass 2: "))

        self.m1 = m1
        self.m2 = m2

    def draw(self):

        p1 = (self.v1x ** 2 + self.v1y ** 2) ** 0.5 * self.m1
        p2 = (self.v2x ** 2 + self.v2y ** 2) ** 0.5 * self.m2
        pt = p1 + p2

        print("Total Momentum: {} kgm/s".format(pt))

        win = Collisions.window(self)

        h1 = random.randint(self.m1*2, self.size - self.m1*2)
        h2 = random.randint(self.m2*2, self.size - self.m2*2)
        # h1 = self.m1+51
        # h2 = self.size-self.m2-51

        distancex = self.size - 100 - self.m1*2 - self.m2*2
        distancey = h2-h1-self.m1-self.m2

        rect1 = Rectangle(Point(50, h1+self.m1), Point(50+self.m1*2, h1-self.m1))
        rect1.setFill("blue")
        rect2 = Rectangle(Point(self.size-50, h2+self.m2), Point(self.size-50-self.m2*2, h2-self.m2))
        rect2.setFill("red")

        left1 = 50
        right1 = -self.size+50+self.m1*2
        top1 = h1-self.m1
        bottom1 = -self.size+h1+self.m1
        left2 = self.size-50-self.m2*2
        right2 = self.size-50
        top2 = h2-self.m2
        bottom2 = -self.size+h2+self.m2

        rect1.draw(win)
        rect2.draw(win)

        while True:

            u1x = self.v1x
            u1y = self.v1y
            u2x = self.v2x
            u2y = self.v2y

            if -2*self.m1-2*self.m2 <= distancex <= 0:
                ycheck = True
            else:
                ycheck = False

            if -2*self.m1-2*self.m2 <= distancey <= 0:
                xcheck = True
            else:
                xcheck = False

            rect1.move(self.v1x, self.v1y)
            rect2.move(self.v2x, self.v2y)

            right1 += self.v1x
            left1 += self.v1x
            top1 += self.v1y
            bottom1 += self.v1y
            right2 += self.v2x
            left2 += self.v2x
            top2 += self.v2y
            bottom2 += self.v2y

            distancex -= self.v1x-self.v2x
            distancey -= self.v1y-self.v2y

            if right1 >= 0 or left1 <= 0:
                self.v1x *= -1

            if right2 >= self.size or left2 <= 0:
                self.v2x *= -1

            if top1 <= 0 or bottom1 >= 0:
                self.v1y *= -1

            if top2 <= 0 or bottom2 >= 0:
                self.v2y *= -1

            if -2*self.m1-2*self.m2 <= distancey <= 0 and ycheck:
                if -2*self.m1-2*self.m2 <= distancex <= 0:
                    self.v1y = (self.m1**2-self.m2**2)/(self.m1**2+self.m2**2)*u1y + \
                               (2*self.m2**2)/(self.m1**2+self.m2**2)*u2y
                    self.v2y = (self.m2**2-self.m1**2)/(self.m1**2+self.m2**2)*u2y + \
                               (2*self.m1**2)/(self.m1**2+self.m2**2)*u1y

            if -2*self.m1-2*self.m2 <= distancex <= 0 and xcheck:
                if -2*self.m1-2*self.m2 <= distancey <= 0:
                    self.v1x = (self.m1-self.m2)/(self.m1+self.m2)*u1x + (2*self.m2)/(self.m1+self.m2)*u2x
                    self.v2x = (self.m2-self.m1)/(self.m1+self.m2)*u2x + (2*self.m1)/(self.m1+self.m2)*u1x

            if win.checkMouse():
                win.close()

            sleep(0.01)


start = Collisions()
start.define()
start.draw()

