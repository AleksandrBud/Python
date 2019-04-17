# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person(object):
    def __init__(self, i_health, i_damage, i_armor):
        self.name = str(input('Введите имя игрока: '))
        self.health = float(i_health)
        self.damage = float(i_damage)
        self.armor = float(i_armor)

    def calc_damage(self, i_dem):
        return i_dem / self.armor


class Player(Person):
    def __init__(self):
        super().__init__(100, 20, 1.5)

    def attack(self, i_attacker, i_attack):
        i_attack.health = i_attack.health - i_attack.calc_damage(i_attacker.damage)

class Enemy(Person):
    def __init__(self):
        super().__init__(70, 35, 1.3)

    def attack(self, i_attacker, i_attack):
        i_attack.health = i_attack.health - i_attack.calc_damage(i_attacker.damage)


class Game(object):
    def __init__(self):
        self.pl1 = Player()
        self.pl2 = Enemy()

    def start_game(self):
        while self.pl1.health > 0 or self.pl2.health > 0:
            self.pl1.attack(self.pl1, self.pl2)
            self.pl2.attack(self.pl2, self.pl1)
            print(self.pl1.health, self.pl2.health)
        print('End')


game = Game()
game.start_game()