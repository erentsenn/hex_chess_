from Field import Field
from check import input_to_move


def Chess():
    f = Field() # инициализируем поле
    player = 'white' #текущий игрок, белые - маленькие буквы
    while True:

        f.print_field() # на каждом ходе выводим поле
        print(player, 'move')
        input_to_move(player, f) # получаем от пользователя координаты фигуры, которой хотим ходить
        if 'k' not in f.field.values(): # на каждом ходу првоеряем есть ли король на поле, если его срубили то игра заканчивается
            f.print_field()
            print('BLACK WIN')
            break

        if 'K' not in f.field.values():
            f.print_field()
            print('WHITE WIN')
            break

        if player == 'white': # меняем ход
            player = 'black'
        else:
            player = 'white'


if __name__ == '__main__':
    Chess()
