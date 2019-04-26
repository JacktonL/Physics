from graphics import GraphWin, Circle, Point
from time import sleep
from random import randint


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

        if not i == cir:
            if abs(i.py-cir.py) <= cir.m*1.2:
                if abs(i.px-cir.px) <= cir.m*1.2:

                    cir.vx = (cir.m-i.m)/(cir.m+i.m)*u1x + (2*i.m)/(cir.m+i.m)*u2x
                    cir.vy = (cir.m-i.m)/(cir.m+i.m)*u1y + (2*i.m)/(cir.m+i.m)*u2y
                    i.vx = (i.m-cir.m)/(cir.m+i.m)*u2x + (2*cir.m)/(cir.m+i.m)*u1x
                    i.vy = (i.m-cir.m)/(cir.m+i.m)*u2y + (2*cir.m)/(cir.m+i.m)*u1y


while True:
    vx = randint(-3, 3)
    vy = randint(-3, 5)

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
