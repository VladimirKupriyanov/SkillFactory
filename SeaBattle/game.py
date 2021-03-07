from random import randint
from inner_logic import *


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input('Ваш ход: ').split()
            if len(cords) != 2:
                print(' Введите 2 координаты! ')
                continue
            x, y = cords[0], cords[1].upper()
            if not (x.isdigit()) or y not in Board.letters:
                print(' Не верный ввод! ')
                continue
            x, y = int(x), Board.letters.index(y)
            return Dot(x - 1, y)


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    @staticmethod
    def greet():
        print('-' * 61)
        print('МОРСКОЙ БОЙ'.center(61))
        print('-' * 61)
        print('формат ввода: x y'.center(61))
        print('x - номер строки, y - буква столбца'.center(61))

    def loop(self):
        num = 0
        while True:
            print('-' * 61)
            print('Доска пользователя:'.center(27) + '   |   ' + 'Доска компьютера:'.center(27))
            us_st = str(self.us.board).split('\n')
            ai_st = str(self.ai.board).split('\n')
            res_st = ''
            for i in range(len(us_st)):
                res_st += us_st[i] + '   |   ' + ai_st[i] + '\n'
            print(res_st)
            print('-' * 61)
            if num % 2 == 0:
                print('Ходит пользователь!')
                repeat = self.us.move()
            else:
                print('Ходит компьютер!')
                repeat = self.ai.move()
            if repeat:
                num -= 1
            if self.ai.board.count == 7:
                print('Пользователь выиграл!')
                break
            if self.us.board.count == 7:
                print('Компьютер выиграл!')
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()

if __name__ == '__main__':
    g = Game()
    g.start()
