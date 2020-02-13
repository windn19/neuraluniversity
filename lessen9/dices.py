from random import randint

'''
Игра в кости. Компьютер загадывает два числа от 1 до 6(кидает кости).
Дальше кидает игрок. Так же кидает кости, если 1 - полностью совпадают  - выйгрыш. 
                                               2 - если одна цифра сопадает,
                                               3 - сумма цифр совпадает. 
данные: бросок компьютера,
        бросок игрока, 
        тип игры.
методы: определение цифр компьютера.
        игра
        определение выйгрыша.
'''


class Dice:
    def __init__(self, number_throw=1, type_game=1):
        self.computer_throw = []
        self.human_throw = []
        self.amount = number_throw
        self.type = type_game

    def define_computer(self):
        self.computer_throw = (randint(1, 6), randint(1, 6))

    def winner(self):
        if self.type == 1:
            return set(self.human_throw) == set(self.computer_throw)
        elif self.type == 2:
            return self.human_throw[0] in self.computer_throw or self.human_throw[1] in self.computer_throw
        else:
            return sum(self.computer_throw) == sum(self.human_throw)

    def run(self):
        self.define_computer()
        for _ in range(self.amount):
            self.human_throw = (randint(1, 6), randint(1, 6))
            print(f'Выпало {self.human_throw}')
            if self.winner():
                print('You are winner!!!')
                break
            else:
                print("No lucky")
        print(f'У компьтера выпало - {self.computer_throw}')


temp = Dice(type_game=2, number_throw=5)
temp.run()
