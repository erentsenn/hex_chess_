from Field import check_pos_on_field

"""
Шаблон нахождения всех фигур -
получаем координаты фигуры ->
Перебираем возможные поля, на которые можно пойти по правилам игры и проверяем их на доступность"""
class Figure:
    symbols = ''

    def get_symbols(self):
        return self.symbols


class PawnWhite(Figure):

    def __init__(self):
        self.symbols = 'p'

    def get_all_movies(self, i, j, field):
        arr_ret = set()
        if field[(i, j + 1)] == '.':
            arr_ret.add((i, j + 1))
        alf = 'ABCDEFGHIKL'
        # (alf[alf.index(a_ind) + 1], i_ind + 3)
        if 'F' > i > 'A' and field[(alf[alf.index(i) - 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) - 1], j))
        if 'F' > i and field[(alf[alf.index(i) + 1], j + 1)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) + 1], j + 1))

        if i == 'F' and field[(alf[alf.index(i) - 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) - 1], j))

        if 'F' == i and field[(alf[alf.index(i) + 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) + 1], j))

        if 'F' < i < 'L' and field[(alf[alf.index(i) + 1], j)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) + 1], j))
        if i > 'F' and field[(alf[alf.index(i) - 1], j + 1)] in list('PRNBQK'):
            arr_ret.add((alf[alf.index(i) - 1], j + 1))
        return list(arr_ret)


class PawnBlack(Figure):

    def __init__(self):
        self.symbols = 'P'

    def get_all_movies(self, i, j, field):
        arr_ret = set()
        if field[(i, j - 1)] == '.':
            arr_ret.add((i, j - 1))
        alf = 'ABCDEFGHIKL'
        # (alf[alf.index(a_ind) + 1], i_ind + 3)
        if 'F' > i > 'A' and field[(alf[alf.index(i) - 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) - 1], j - 1))
        if 'F' > i and field[(alf[alf.index(i) + 1], j)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) + 1], j))

        if i == 'F' and field[(alf[alf.index(i) - 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) - 1], j - 1))

        if 'F' == i and field[(alf[alf.index(i) + 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) + 1], j - 1))

        if 'F' < i < 'L' and field[(alf[alf.index(i) + 1], j - 1)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) + 1], j - 1))
        if i > 'F' and field[(alf[alf.index(i) - 1], j)] in list('PRNBQK'.lower()):
            arr_ret.add((alf[alf.index(i) - 1], j))
        return list(arr_ret)


class RookWhite(Figure):

    def __init__(self):
        self.symbols = 'r'

    def get_all_movies(self, a_ind, i_ind, field):
        arr_ret = set()
        answ = set()
        for i in range(i_ind + 1, 12):
            if field[(a_ind, i)] == '.':

                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'):
                    answ.add((a_ind, i))
                break

        for i in range(i_ind - 1, 0, -1):
            if field[(a_ind, i)] == '.':
                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'):
                    answ.add((a_ind, i))
                break

        if a_ind == 'F':
            new_i = i_ind
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i = i_ind - 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        ###################################################################
        elif a_ind > 'F':
            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F')::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1::]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

        elif a_ind < 'F':
            new_i = i_ind
            if a_ind > 'A':
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                        elif field[(a, new_i)] in list('PRHEQK'):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            break
                    except:
                        pass
            if a_ind > 'A':
                new_i = i_ind - 1
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                            new_i -= 1
                        elif field[(a, new_i)] in list('PRHEQK'):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            break
                    except:
                        pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        return list(answ)


class RookBlack(Figure):

    def __init__(self):
        self.symbols = 'R'

    def get_all_movies(self, a_ind, i_ind, field):
        arr_ret = set()
        answ = set()
        for i in range(i_ind + 1, 12):
            if field[(a_ind, i)] == '.':

                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'.lower()):
                    answ.add((a_ind, i))
                break

        for i in range(i_ind - 1, 0, -1):
            if field[(a_ind, i)] == '.':
                answ.add((a_ind, i))
            else:
                if field[(a_ind, i)] in list('PRHEQK'.lower()):
                    answ.add((a_ind, i))
                break

        if a_ind == 'F':
            new_i = i_ind
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i = i_ind - 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        ###################################################################
        elif a_ind > 'F':
            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F')::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1::]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

        elif a_ind < 'F':
            new_i = i_ind
            if a_ind > 'A':
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'):
                            break
                    except:
                        pass
            if a_ind > 'A':
                new_i = i_ind - 1
                for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                    try:
                        if field[(a, new_i)] == '.':
                            answ.add((a, new_i))
                            new_i -= 1
                        elif field[(a, new_i)] in list('PRHEQK'.lower()):
                            answ.add((a, new_i))
                            break
                        elif field[(a, new_i)] in list('PRHEQK'):
                            break
                    except:
                        pass

            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1  ###
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        return list(answ)


class BishopWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()

        arr_ret = set()

        if a_ind == 'A':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('L', 0 + i_ind))
        elif a_ind == 'B':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('K', i_ind))
        elif a_ind == 'C':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('I', i_ind))
        elif a_ind == 'D':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('H', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('H', i_ind))
                arr_ret.add(('K', i_ind - 1))
        elif a_ind == 'E':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('G', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'F':
            if i_ind in [2, 10]:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
            else:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
                arr_ret.add(('B', i_ind - 2))
                arr_ret.add(('K', i_ind - 2))

        elif a_ind == 'G':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('E', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'H':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('D', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('D', i_ind))
                arr_ret.add(('K', i_ind - 1))

        elif a_ind == 'I':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('C', i_ind))

        elif a_ind == 'L':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('A', i_ind))

        elif a_ind == 'K':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('B', i_ind))

        last = 0
        for alf in 'ABCDEFGHIKL'[::2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'.lower()):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        last = 0
        for alf in 'ABCDEFGHIKL'[::-2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'.lower()):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        # diagonals
        #####################################################################
        if a_ind == 'F':
            new_i = i_ind + 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i = i_ind + 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        #######################################################
        elif a_ind > 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass
        #########################################################################
        elif a_ind < 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        break
                except:
                    pass

        return list(answ)


class BishopBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()

        arr_ret = set()

        if a_ind == 'A':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('L', 0 + i_ind))
        elif a_ind == 'B':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('K', i_ind))
        elif a_ind == 'C':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('I', i_ind))
        elif a_ind == 'D':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('H', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('H', i_ind))
                arr_ret.add(('K', i_ind - 1))
        elif a_ind == 'E':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('G', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('G', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'F':
            if i_ind in [2, 10]:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
            else:
                arr_ret.add(('D', i_ind - 1))
                arr_ret.add(('H', i_ind - 1))
                arr_ret.add(('B', i_ind - 2))
                arr_ret.add(('K', i_ind - 2))

        elif a_ind == 'G':
            if i_ind == 1 or i_ind == 10:
                arr_ret.add(('E', i_ind))
            elif i_ind == 2 or i_ind == 9:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
            else:
                arr_ret.add(('C', i_ind - 1))
                arr_ret.add(('A', i_ind - 2))
                arr_ret.add(('E', i_ind))
                arr_ret.add(('I', i_ind - 1))
                arr_ret.add(('L', i_ind - 2))

        elif a_ind == 'H':
            if i_ind in [1, 9]:
                arr_ret.add(('F', 1 + i_ind))
                arr_ret.add(('D', i_ind))
            else:
                arr_ret.add(('B', i_ind - 1))
                arr_ret.add(('F', i_ind + 1))
                arr_ret.add(('D', i_ind))
                arr_ret.add(('K', i_ind - 1))

        elif a_ind == 'I':
            if i_ind != 1 and i_ind != 8:
                arr_ret.add(('A', i_ind - 1))
                arr_ret.add(('L', i_ind - 1))
            arr_ret.add(('E', 1 + i_ind))
            arr_ret.add(('G', 1 + i_ind))
            arr_ret.add(('C', i_ind))

        elif a_ind == 'L':
            arr_ret.add(('C', 1 + i_ind))
            arr_ret.add(('E', 2 + i_ind))
            arr_ret.add(('G', 2 + i_ind))
            arr_ret.add(('I', 1 + i_ind))
            arr_ret.add(('A', i_ind))

        elif a_ind == 'K':
            arr_ret.add(('D', 1 + i_ind))
            arr_ret.add(('F', 2 + i_ind))
            arr_ret.add(('H', 1 + i_ind))
            arr_ret.add(('B', i_ind))

        last = 0
        for alf in 'ABCDEFGHIKL'[2::2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'.lower()):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        last = 0
        for alf in 'ABCDEFGHIKL'[- 2::-2]:
            for pos in arr_ret:
                if alf in pos:
                    if field[pos] == '.':
                        answ.add(pos)
                    elif field[pos] in list('PRHEQK'.lower()):
                        answ.add(pos)
                        last = pos
                        break
                    elif field[pos] in list('PRHEQK'):
                        last = pos
                        break
            if last != 0 and (field[last] in list('PRHEQK') or field[last] in list('PRHEQK'.lower())):
                break

        # diagonals
        #####################################################################
        if a_ind == 'F':
            new_i = i_ind + 1
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'GHIKL':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i = i_ind + 1
            for a in 'EDCBA':
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        #######################################################
        elif a_ind > 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1:'ABCDEFGHIKL'.index('F') - 1:-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass
        #########################################################################
        elif a_ind < 'F':
            new_i = i_ind + 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) - 1::-1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind + 2
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i += 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i = i_ind - 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index(a_ind) + 1:'ABCDEFGHIKL'.index('F') + 1]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 1
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

            new_i -= 1
            for a in 'ABCDEFGHIKL'['ABCDEFGHIKL'.index('F') + 1:]:
                try:
                    if field[(a, new_i)] == '.':
                        answ.add((a, new_i))
                        new_i -= 2
                    elif field[(a, new_i)] in list('PRHEQK'.lower()):
                        answ.add((a, new_i))
                        break
                    elif field[(a, new_i)] in list('PRHEQK'):
                        break
                except:
                    pass

        return list(answ)


class KingWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        answ.add((a_ind, i_ind + 1))
        answ.add((a_ind, i_ind - 1))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))
        elif a_ind > 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))

        elif a_ind < 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))

        arr_ret = []
        for pos in parce_pos(answ):
            if field[pos] not in list('PRNBQK'.lower()):
                arr_ret.append(pos)

        return arr_ret


class KingBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        answ.add((a_ind, i_ind + 1))
        answ.add((a_ind, i_ind - 1))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))
        elif a_ind > 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))

        elif a_ind < 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 1))

        arr_ret = []
        for pos in answ:
            try:
                if field[pos] not in list('PRNBQK'):
                    arr_ret.append(pos)
            except:
                pass

        return arr_ret


class KnightWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        if a_ind == 'A':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
        if a_ind == 'B':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))

        if a_ind == 'C':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))

        if a_ind == 'D':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'E':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'G':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))

        if a_ind == 'H':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'I':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'K':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'L':
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        arr_ret = []
        for pos in parce_pos(answ):
            if field[pos] not in 'PRNBQK'.lower():
                arr_ret.append(pos)

        return arr_ret


class KnightBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        answ = set()
        alf = 'ABCDEFGHIKL'
        if a_ind == 'A':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
        if a_ind == 'B':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))

        if a_ind == 'C':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))

        if a_ind == 'D':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'E':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'F':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 2))

        if a_ind == 'G':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind - 1))

        if a_ind == 'H':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 1))
            answ.add((alf[alf.index(a_ind) + 3], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'I':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 2], i_ind + 1))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) + 2], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'K':
            answ.add((alf[alf.index(a_ind) + 1], i_ind + 2))
            answ.add((alf[alf.index(a_ind) + 1], i_ind - 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        if a_ind == 'L':
            answ.add((alf[alf.index(a_ind) - 1], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 1], i_ind - 2))
            answ.add((alf[alf.index(a_ind) - 2], i_ind + 3))
            answ.add((alf[alf.index(a_ind) - 2], i_ind - 1))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 2))
            answ.add((alf[alf.index(a_ind) - 3], i_ind + 1))

        arr_ret = []
        for pos in parce_pos(answ):
            if field[pos] not in 'PRNBQK':
                arr_ret.append(pos)

        return arr_ret


class QueenWhite:
    def get_all_movies(self, a_ind, i_ind, field):
        arr1 = parce_pos(RookWhite().get_all_movies(a_ind, i_ind, field))
        arr2 = parce_pos(BishopWhite().get_all_movies(a_ind, i_ind, field))
        return arr1 + arr2


class QueenBlack:
    def get_all_movies(self, a_ind, i_ind, field):
        arr1 = parce_pos(RookBlack().get_all_movies(a_ind, i_ind, field))
        arr2 = parce_pos(BishopBlack().get_all_movies(a_ind, i_ind, field))
        return arr1 + arr2


def parce_pos(arr):
    arr_ret = []
    for pos in arr:
        if check_pos_on_field(*pos):
            arr_ret.append(pos)

    return arr_ret
