from graphics import GraphWin, Rectangle, Point
from time import sleep
from random import randint


class Windows:

    def __init__(self):

        self.size = 400
        self.win1 = GraphWin("Window 1", self.size, self.size)
        self.win2 = GraphWin("Window 2", self.size, self.size)
        self.vx = randint(3, 7)
        self.vy = randint(3, 7)
        self.m = 15

    def draw(self):

        rect1 = Rectangle(Point(50, 50+self.m), Point(50+self.m*2, 50-self.m))
        rect2 = Rectangle(Point(50-self.size, 50+self.m), Point(50+self.m*2-self.size, 50-self.m))
        rect1.setFill("red")
        rect2.setFill("red")
        rect1.draw(self.win1)
        rect2.draw(self.win2)

        right = -2*self.size + 50 + 2*self.m
        left = 50
        top = 50-self.m
        bottom = -self.size+50+self.m

        while True:

            rect1.move(self.vx, self.vy)
            rect2.move(self.vx, self.vy)

            right += self.vx
            left += self.vx
            top += self.vy
            bottom += self.vy

            if right >= 0:
                self.vx *= -1

            if left <= 0:
                self.vx *= -1

            if top <= 0:
                self.vy *= -1

            if bottom >= 0:
                self.vy *= -1

            sleep(0.01)


win = Windows()
win.draw()