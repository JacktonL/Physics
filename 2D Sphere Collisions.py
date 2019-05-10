from graphics import GraphWin, Circle, Point
from time import sleep
from random import randint
from math import sqrt
import numpy as np


class Circles(Circle):

    def __init__(self, x, y, vx, vy):
        self.size = 500
        self.px = x
        self.py = y
        self.m = 20
        self.vx = vx
        self.vy = vy
        Circle.__init__(self, Point(self.px, self.py), self.m)

    def top(self):
        if self.py - self.m <= 0:
            return True
        return False

    def bottom(self):
        if self.py + self.m >= self.size:
            return True
        return False

    def right(self):
        if self.px + self.m >= self.size:
            return True
        return False

    def left(self):
        if self.px - self.m <= 0:
            return True
        return False


size = 500
win = GraphWin("Collions", size, size)

colors = ["blue", "red", "lime", "orange", "pink", "purple", "brown", "black", "grey", "olive"]

vx = randint(2, 5)
vy = randint(2, 5)

cirObjs = []


def move(cir):
    cir.move(cir.vx, cir.vy)
    cir.px += cir.vx
    cir.py += cir.vy
    if cir.top() or cir.bottom():
        cir.vy *= -1
    if cir.right() or cir.left():
        cir.vx *= -1

    for i in cirObjs:

        u1x = cir.vx
        u1y = cir.vy
        u2x = i.vx
        u2y = i.vy

        u1 = np.array([u1y, u1x])
        u2 = np.array([u2y, u2x])

        yd = i.py-cir.py
        xd = i.px-cir.px

        x1 = np.array([cir.py, cir.px])
        x2 = np.array([i.py, i.px])

        dist = sqrt(yd**2+xd**2)
        if not i == cir:
            if dist <= 2*cir.m:
                y1 = u1 - np.dot(u1-u2, x1-x2)/np.linalg.norm(x1-x2, ord=2)**2*(x1-x2)
                y2 = u2 - np.dot(u2 - u1, x2 - x1) / np.linalg.norm(x2 - x1, ord=2) ** 2 * (x2 - x1)
                cir.vy = y1[0]
                cir.vx = y1[1]
                i.vy = y2[0]
                i.vx = y2[1]


while True:
    vx = randint(-3, 3)
    vy = randint(-3, 3)

    for i in cirObjs:
        move(i)

    p = win.checkMouse()
    if p:

        c1 = Circles(p.getX(), p.getY(), vx, vy)
        color = colors[randint(0, len(colors)-1)]
        c1.setFill(color)
        c1.draw(win)
        cirObjs.append(c1)

    sleep(0.01)
