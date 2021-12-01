class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'{self.__surname} {self.__name}'

class Employee(Person):
    def calc_salary(self):
        pass


class Manager(Employee):
    def calc_salary(self):
        salary = 13000
        return salary


class Agent(Employee):
    def __init__(self, name, surname, age, volume_of_sales):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def calc_salary(self):
        salary = 5000 + (self.volume_of_sales / 100) * 5
        return salary


class Worker(Employee):
    def __init__(self, name, surname, age, hours_worked):
        super().__init__(name, surname, age)
        self.hours_worked = hours_worked

    def calc_salary(self):
        salary = 100 * self.hours_worked
        return salary


persons_lst = []
persons_lst.append(Manager('Vasya', 'Vasev', 44))
persons_lst.append(Manager('Vasya', 'Gasev', 45))
persons_lst.append(Manager('Vasya', 'Tasev', 46))
persons_lst.append(Agent('Petya', 'Petev', 24, 105))
persons_lst.append(Agent('Petya', 'Getev', 25, 212))
persons_lst.append(Agent('Petya', 'Tetev', 26, 345))
persons_lst.append(Worker('Misha', 'Mishev', 34, 52))
persons_lst.append(Worker('Misha', 'Gishev', 35, 62))
persons_lst.append(Worker('Misha', 'Tishev', 36, 72))

for person in persons_lst:
    print(person, 'has salary:',
          '{:.2f}'.format(person.calc_salary()))
