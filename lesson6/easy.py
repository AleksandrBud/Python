# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class Car(object):
    def __init__(self, i_color, i_name):
        self.color = i_color
        self.name = i_name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, i_directon):
        print('Машина повернула ' + str(i_directon))


class TownCar(Car):
    def __init__(self, i_color, i_name):
        super().__init__(i_color, i_name)
        self.speed = 100
        self.is_police = False


class SportCar(Car):
    def __init__(self, i_color, i_name):
        super().__init__(i_color, i_name)
        self.speed = 160
        self.is_police = False


class WorkCar(Car):
    def __init__(self, i_color, i_name):
        super().__init__(i_color, i_name)
        self.speed = 120
        self.is_police = False


class PoliceCar(Car):
    def __init__(self, i_color, i_name):
        super().__init__(i_color, i_name)
        self.speed = 140
        self.is_police = True


town_car = TownCar('Серый', 'Имя1')
sport_car = SportCar('Красный', 'Имя2')
work_car = WorkCar('Черный', 'Имя3')
police_car = PoliceCar('Белый', 'Имя3')

print(town_car.speed)
print(police_car.is_police)
print(sport_car.speed)
print(work_car.is_police)
work_car.go()
sport_car.turn('направо')