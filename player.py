from turtle import Turtle


class Player(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.__x = x
        self.__y = y
        self.goto(self.__x, self.__y)
        self.shape("turtle")
        self.setheading(90)
        self.shapesize(0.8)
        self.color("black")
        self.showturtle()

    def move(self):
        new_y = self.ycor() + 30
        self.goto(0, new_y)

    def check_proceed_to_next_level(self):
        if self.ycor() > 300:
            self.goto(self.__x, self.__y)
            return True
        return False
