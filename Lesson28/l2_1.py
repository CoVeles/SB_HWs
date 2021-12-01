class Robot:
    def __init__(self, model='N/A'):
        self.model = model

    def operate(self):
        print('Я - Робот')


class CanFly:
    def __init__(self):
        self.height = 0
        self.__speed = 0
        self.__distance = 0

    def take_off(self):
        self.height = 1000

    def fly(self):
        self.__speed = 500
        self.__distance = 100

    def land_on(self):
        self.height = 0
        self.__speed = 0


class ReconDrone(Robot, CanFly):
    def __init__(self, model='RD#'):
        super().__init__(model)

    def operate(self):
        self.take_off()
        self.fly()
        print('Веду разведку с воздуха')


class FlyingWarRobot(Robot, CanFly):
    def __init__(self, model='WR#', gun='Pistol'):
        super().__init__(model)
        self.__gun = gun

    def operate(self):
        self.take_off()
        print(
            self.model,
            'высота',
            self.height,
            'Защита военного объекта с воздуха с помощью',
            self.__gun
        )


r = Robot('wally')
r.operate()
rd = ReconDrone()
rd.operate()
wr = FlyingWarRobot()
wr.operate()





