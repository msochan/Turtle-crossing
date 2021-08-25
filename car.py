from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.__red = random.randint(1, 255)
        self.__green = random.randint(1, 255)
        self.__blue = random.randint(1, 255)
        self.shape("square")
        self.fillcolor(self.__red, self.__green, self.__blue)
        self.pencolor(self.__red, self.__green, self.__blue)
        self.turtlesize(stretch_len=2)
        y = random.randint(x, y)
        self.goto(310, y)
        self.showturtle()
