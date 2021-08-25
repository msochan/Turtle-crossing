import random


class CarManager:
    def __init__(self):
        self.__car_list = []
        self.__car_speed = 5

    def add_car(self, car):
        random_num = random.randint(2, 4)
        # print(random_num)
        if len(self.__car_list) < 50 and random_num == 3 or random_num == 4:
            self.__car_list.append(car)
            car.goto(car.xcor(), car.ycor())

    def move_car(self):
        for car in self.__car_list:
            if car.xcor() < -300:
                self.__car_list.remove(car)
            new_x = car.xcor() - self.__car_speed
            car.goto(new_x, car.ycor())

    def increase_car_speed(self):
        self.__car_speed += 5

    def get_cars_list(self):
        return self.__car_list

    def check_collision(self, player):
        for car in self.__car_list:
            if car.distance(player) < 20:
                return True
        return False
