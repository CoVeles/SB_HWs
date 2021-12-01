from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    @abstractmethod
    def move(self, distance):
        print('Move', end=' ')

    @abstractmethod
    def beep(self):
        print('beep', end=' ')


class PlayMusicMixin:
    def play_music(self):
        print('Playing music')


class Auto(Transport):
    def move(self, distance):
        super().move(distance)
        print('on earth')

    def beep(self):
        super().beep()
        print('Auto')


class Amphibian(Transport, PlayMusicMixin):
    def move(self, distance):
        super().move(distance)
        print('on earth and water')

    def beep(self):
        super().beep()
        print('Amphibian')


class Boat(Transport):
    def move(self, distance):
        super().move(distance)
        print('on water')

    def beep(self):
        super().beep()
        print('Boat')


a = Auto('red', 50)
print(a.color)
am = Amphibian('blue', 30)
b = Boat('yellow', 20)
a.move(24)
a.beep()
am.play_music()
b.move(23)
