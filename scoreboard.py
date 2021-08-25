from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__level = 1
        self.hideturtle()
        self.penup()
        self.goto(-180, 250)
        self.color("black")
        self.print_game_info()

    def next_level(self):
        self.clear()
        self.__level += 1
        self.print_game_info()

    def print_game_info(self):
        self.write(f"Level: {self.__level}", align="left", font=("Arial", 30, "normal"))

    @staticmethod
    def print_game_over():
        game_over = Turtle()
        game_over.hideturtle()
        game_over.goto(-150, 0)
        game_over.write(f"GAME OVER", align="left", font=("Arial", 50, "normal"))
