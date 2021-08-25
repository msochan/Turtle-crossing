import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from car import Car
from scoreboard import Scoreboard

PLAYER_START_POS_X = 0
PLAYER_START_POS_Y = -270

screen = Screen()
screen.colormode(255)
player = Player(PLAYER_START_POS_X, PLAYER_START_POS_Y)
car_manager = CarManager()
score_board = Scoreboard()

screen.setup(600, 600)
screen.tracer(0)


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car(Car(PLAYER_START_POS_Y + 30, score_board.ycor() - 30))
    car_manager.move_car()

    # Check collision with cars
    if car_manager.check_collision(player):
        Scoreboard.print_game_over()
        game_is_on = False

    # Check collision with top screen - next level condition
    if player.check_proceed_to_next_level():
        score_board.next_level()
        car_manager.increase_car_speed()

screen.exitonclick()
