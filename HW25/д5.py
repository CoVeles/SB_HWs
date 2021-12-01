import math
import random


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        if angle > 360:
            raise ValueError('Угол задается от 0 до 360')
        self.angle = math.radians(angle)

    def __str__(self):
        return (f'\nМашина находится в координатах'
                f'\nx = {round(self.x, 2)}, '
                f'y = {round(self.y, 2)}')

    def turn(self, angle):
        self.angle = math.radians(angle)

    def move(self, distance):
        self.x = self.x + distance * math.cos(self.angle)
        self.y = self.y + distance * math.sin(self.angle)


class Bus(Car):
    __total_distance = 0

    def __init__(self, x, y, angle, passengers=0, cash=0):
        super().__init__(x, y, angle)
        self.passengers = passengers
        self.cash = cash

    def __str__(self):
        return (f'\nАвтобус находится в координатах'
                f'\nx = {round(self.x, 2)}, '
                f'y = {round(self.y, 2)}'
                f'\nпассажиров = {self.passengers}'
                f'\nполученные деньги = {self.cash}')

    def move(self, distance):
        super().move(distance)
        self.__total_distance += distance
        self.cash += (self.passengers * self.__total_distance * 3)

    def get_on(self):
        self.passengers += random.randint(1, 5)

    def get_off(self):
        if self.passengers > 0:
            self.passengers -= random.randint(1, self.passengers)


car = Car(0, 0, 0)
car.move(5)
print(car)
car.turn(90)
car.move(5)
print(car)
bus = Bus(0, 0, 0)
bus.move(5)
bus.turn(90)
bus.move(5)
bus.get_on()
print(bus)
bus.get_on()
bus.move(5)
print(bus)
bus.get_off()
bus.move(5)
print(bus)
