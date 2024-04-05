from Field import Field
from pieces import *

def check_figure_attack_white(field: dict): # то же самое
    figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': KnightWhite,
                   'N': KnightBlack,
                   'b': BishopWhite, 'B': BishopBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                   'q': QueenWhite}
    arr_ret = set()

    for pos, f in field.items():
        ind_i_from, ind_j_from = pos
        if field[pos] != '.':
            movies = parce_pos(figure_dict[field[(ind_i_from, ind_j_from)]]().get_all_movies(ind_i_from, ind_j_from, field))
            for move in movies:
                if field[move] in 'PRNBQK'.lower():
                    arr_ret.add(move)

    return arr_ret


def check_figure_attack_black(field: dict):
    figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': KnightWhite,
                   'N': KnightBlack,
                   'b': BishopWhite, 'B': BishopBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                   'q': QueenWhite}
    arr_ret = set() # множество всех уязвимых позиций
    for pos, f in field.items(): # проверяем все клетки доски
        ind_i_from, ind_j_from = pos
        if field[pos] != '.': # которые являются фигурами
            movies = parce_pos(figure_dict[field[(ind_i_from, ind_j_from)]]().get_all_movies(ind_i_from, ind_j_from, field))
            # получаем все возможные ходы этой фигуры(значение ячейки)
            for move in movies:
                if field[move] in 'PRNBQK': # и если там стоит фигура врага, она будет добавлена в массив уязвимых фигур
                    arr_ret.add(move)

    return arr_ret


def input_to_move(player, F):
    field = F.field
    while True: # в бесконечном цикле пытаемся считать валидные координаты фигуры
        # ввели позицию фигуры
        if player == 'black': # выводим уязвимые позиции
            print('уязвимые позиции', check_figure_attack_black(field))
        else:
            print('уязвимые позиции', check_figure_attack_white(field))
        while True:
            try:
                inp = input('FROM: ').split()

                ind_i_from, ind_j_from = inp[0].upper(), int(inp[1])
                # hod = a, b
                if field[(ind_i_from, ind_j_from)] in list('prnbqk') and player == 'white':
                    break
                elif field[(ind_i_from, ind_j_from)] in list('prnbqk'.upper()) and player == 'black':
                    break
                else:
                    print('Это не ваша фигура')
            except:
                pass
        # вводим позицию хода
        figure_dict = {'p': PawnWhite, 'P': PawnBlack, 'R': RookBlack, 'r': RookWhite, 'n': KnightWhite,
                       'N': KnightBlack,
                       'b': BishopWhite, 'B': BishopBlack, 'K': KingBlack, 'k': KingWhite, 'Q': QueenBlack,
                       'q': QueenWhite}
        # check_mat(player, field, figure_dict)
        # parce_pos принимает
        movies = parce_pos(figure_dict[field[(ind_i_from, ind_j_from)]]().get_all_movies(ind_i_from, ind_j_from, field))
        if not movies:# если нет доступных ходов, то попытаемся считать другие координаты
            print('Эта фигура не может ходить, выберите другую фигуру')
            continue
        F1 = F.field.copy()
        for pos in movies:
            F1[pos] = '*'
        Field.print_field_copy(F1)
        Field.print_field_copy(F1)
        print('Возможные ходы')
        print(*movies)

        try:
            inp = input('TO: ').split()

            ind_i_to, ind_j_to = inp[0].upper(), int(inp[1])

            # ind_i_to = abs(int(b) - 8)
            # ind_j_to = list('ABCDEFGH').index(a.upper())

            # print(movies)
            if (ind_i_to, ind_j_to) in movies:
                field[(ind_i_to, ind_j_to)] = field[(ind_i_from, ind_j_from)]
                field[(ind_i_from, ind_j_from)] = '.'
                break
            else:
                print('Такой ход невозможен')
        except:
            pass