import random


class DepressionError(Exception):
    pass


class HungerError(Exception):
    pass


class House:
    __total_earnings = 0
    __total_food_eaten = 0
    __total_fur_coats = 0

    def __init__(self):
        self.stash = 100
        self.fridge = 50
        self.cat_food = 30
        self.__dirt = 0

    def __str__(self):
        return (f'House cash= {self.stash}, fridge= {self.fridge}'
                f'cat_food= {self.cat_food}, dirt= {self.__dirt}')

    def reduce_dirt(self, points):
        self.__dirt -= points
        if self.__dirt < 0:
            self.__dirt = 0

    def make_dirt(self, points):
        self.__dirt += points

    def get_dirt(self):
        return self.__dirt

    def add_cash(self, cash):
        self.stash += cash
        self.__total_earnings += cash

    def take_food(self):
        if self.fridge > 30:
            portion = random.randint(10, 30)
        else:
            portion = self.fridge / 2
        self.fridge -= portion
        self.__total_food_eaten += portion
        return portion

    def take_cat_food(self):
        if self.cat_food > 10:
            portion = random.randint(5, 10)
        else:
            portion = self.cat_food
        self.cat_food -= portion
        return portion

    def add_coat_to_wardrobe(self):
        self.__total_fur_coats += 1

    def print_total(self):
        print(f'\nРезультаты за год:'
              f'\nДенег заработано: {self.__total_earnings}'
              f'\nСъедено еды: {self.__total_food_eaten}'
              f'\nШуб куплено: {self.__total_fur_coats}')




class Man:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.happiness = 100
        self.home = home

    def __str__(self):
        return (f'{self.name} satiety= {self.satiety}, '
                f'happy= {self.happiness}')

    def eat(self):
        portion = self.home.take_food()
        if portion == 0:
            raise ValueError
        self.satiety += portion
        self.action()
        print(f'{self.name} eat {portion}')

    def pet_cat(self):
        self.happiness += 5
        self.action()
        print(f'{self.name} pet cat')

    def check_health(self):
        if self.satiety < 0:
            raise HungerError(f'{self.name} died from hunger')
        elif self.happiness < 10:
            raise DepressionError(f'{self.name} died from depression')

    def action(self):
        self.satiety -= 10


class Husband(Man):
    def play(self):
        self.happiness += 20
        self.action()
        print(f'{self.name} play')

    def work(self):
        self.home.add_cash(150)
        self.action()
        print(f'{self.name} work')


class Wife(Man):
    def buy_meal(self):
        if self.home.stash >= 150:
            self.home.fridge += 120
            self.home.cat_food += 30
            self.home.stash -= 150
        else:
            self.home.fridge += self.home.stash
            self.home.stash = 0
        self.action()
        print(f'{self.name} buy meal')

    def buy_coat(self):
        if self.home.stash >= 350:
            self.home.add_coat_to_wardrobe()
            self.home.stash -= 350
            self.satiety += 60
            self.action()
            print(f'{self.name} buy coat')

    def clean_house(self):
        self.home.reduce_dirt(100)
        self.action()
        print(f'{self.name} clean house')

class Cat:
    def __init__(self, name, home):
        self.name = name
        self.satiety = 30
        self.home = home

    def __str__(self):
        return f'{self.name}, satiety= {self.satiety}'

    def eat(self):
        portion = self.home.take_cat_food()
        if portion == 0:
            raise ValueError
        self.satiety += portion * 2
        print(f'{self.name} eat {portion}')

    def sleep(self):
        self.satiety -= 10
        print(f'{self.name} sleep')

    def tear_wallpaper(self):
        self.satiety -= 10
        self.home.reduce_dirt(5)
        print(f'{self.name} tear wallpaper')

    def check_health(self):
        if self.satiety < 0:
            raise HungerError(f'{self.name} died from hunger')


def husband_day(husband):
    if husband.satiety < 21:
        try:
            husband.eat()
        except ValueError:
            husband.work()
    elif husband.home.stash < 150:
        husband.work()
    else:
        if husband.happiness < 21:
            if random.randint(1, 10) == 1:
                husband.pet_cat()
            else:
                husband.play()
        else:
            husband.work()
    if husband.home.get_dirt() > 90:
        husband.happiness -= 10
    print(husband)


def wife_day(wife):
    if wife.satiety < 21 and wife.home.fridge > 10:
        try:
            wife.eat()
        except ValueError:
            wife.buy_meal()
    elif wife.home.fridge < 40 or wife.home.cat_food < 10:
        wife.buy_meal()
    elif wife.home.get_dirt() > 80:
        wife.clean_house()
    else:

        if random.randint(1, 10) == 1:
            wife.pet_cat()
        elif wife.home.stash > 350:
            wife.buy_coat()
        else:
            wife.eat()

    if wife.home.get_dirt() > 90:
        wife.happiness -= 10
    print(wife)


def cat_day(cat):
    if cat.satiety < 11:
        try:
            cat.eat()
        except ValueError:
            cat.sleep()
    elif random.randint(1, 10) == 1:
        cat.tear_wallpaper()
    else:
        cat.sleep()


home = House()
residents = [Husband('Husband', home),
             Wife('Wife', home),
             Cat('Cat', home)]

total_coats = total_cash = total_food = 0
for i in range(1, 366):
    print(f'\nDay {i}')
    home.make_dirt(5)

    for resident in residents:
        if isinstance(resident, Husband):
            husband_day(resident)
        elif isinstance(resident, Wife):
            wife_day(resident)
        else:
            cat_day(resident)
        try:
            resident.check_health()
        except Exception as err:
            print(err)
            residents.remove(resident)
    print(home)
    if not residents:
        break

if not residents:
    print('\nAll died!')
else:
    home.print_total()
