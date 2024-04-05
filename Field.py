class Field: # класс доски
    def __init__(self):
        self.field = {}
        for a in 'ABCDEFGHIKL':
            for i in range(1, 12):
                self.field[(a, i)] = '.'
        for a in 'ABCDEFGHIKL':
            self.field[(a, 7)] = 'P'

        self.field[('F', 5)] = 'p'
        self.field[('E', 4)] = 'p'
        self.field[('G', 4)] = 'p'
        self.field[('D', 3)] = 'p'
        self.field[('H', 3)] = 'p'
        self.field[('C', 2)] = 'p'
        self.field[('I', 2)] = 'p'
        self.field[('B', 1)] = 'p'
        self.field[('K', 1)] = 'p'

        self.field[('C', 1)], self.field[('I', 1)] = 'r', 'r'
        self.field[('C', 8)], self.field[('I', 8)] = 'R', 'R'

        self.field[('F', 1)], self.field[('F', 2)], self.field[('F', 3)] = 'b', 'b', 'b'
        self.field[('F', 11)], self.field[('F', 10)], self.field[('F', 9)] = 'B', 'B', 'B'

        self.field[('D', 1)], self.field[('H', 1)] = 'n', 'n'
        self.field[('D', 9)], self.field[('H', 9)] = 'N', 'N'

        self.field[('E', 1)], self.field[('G', 1)] = 'q', 'k'
        self.field[('E', 10)], self.field[('G', 10)] = 'Q', 'K'

    def print_field(self): # выводит доску
        print(f"         11   11    ")
        print(f"       10   {self.field[('F', 11)]}   10")
        print(f"      9   {self.field[('E', 10)]}   {self.field[('G', 10)]}   9")
        print(f"    8   {self.field[('D', 9)]}   {self.field[('F', 10)]}   {self.field[('H', 9)]}   8")
        print(
            f"  7   {self.field[('C', 8)]}   {self.field[('E', 9)]}   {self.field[('G', 9)]}   {self.field[('I', 8)]}   7")
        for i in range(7, 1, -1):
            print(
                f"{i - 1}   {self.field[('B', i)]}   {self.field[('D', i + 1)]}   {self.field[('F', i + 2)]}   {self.field[('H', i + 1)]}   {self.field[('K', i)]}   {i - 1}")
            print(
                f"  {self.field[('A', i - 1)]}   {self.field[('C', i)]}   {self.field[('E', i + 1)]}   {self.field[('G', i + 1)]}   {self.field[('I', i)]}   {self.field[('L', i - 1)]}")

        print(
            f"  a {self.field[('B', 1)]}   {self.field[('D', 2)]}   {self.field[('F', 3)]}   {self.field[('H', 2)]}   {self.field[('K', 1)]} l")
        print(
            f"    b {self.field[('C', 1)]}   {self.field[('E', 2)]}   {self.field[('G', 2)]}   {self.field[('I', 1)]} k")
        print(f"      c {self.field[('D', 1)]}   {self.field[('F', 2)]}   {self.field[('H', 1)]} i")
        print(f"        d {self.field[('E', 1)]}   {self.field[('G', 1)]} h")
        print(f"          e {self.field[('F', 1)]} g")
        print(f"            f")

    @classmethod
    def print_field_copy(self, field):
        print(f"         11   11    ")
        print(f"       10   {field[('F', 11)]}   10")
        print(f"      9   {field[('E', 10)]}   {field[('G', 10)]}   9")
        print(f"    8   {field[('D', 9)]}   {field[('F', 10)]}   {field[('H', 9)]}   8")
        print(
            f"  7   {field[('C', 8)]}   {field[('E', 9)]}   {field[('G', 9)]}   {field[('I', 8)]}   7")
        for i in range(7, 1, -1):
            print(
                f"{i - 1}   {field[('B', i)]}   {field[('D', i + 1)]}   {field[('F', i + 2)]}   {field[('H', i + 1)]}   {field[('K', i)]}   {i - 1}")
            print(
                f"  {field[('A', i - 1)]}   {field[('C', i)]}   {field[('E', i + 1)]}   {field[('G', i + 1)]}   {field[('I', i)]}   {field[('L', i - 1)]}")

        print(
            f"  a {field[('B', 1)]}   {field[('D', 2)]}   {field[('F', 3)]}   {field[('H', 2)]}   {field[('K', 1)]} l")
        print(
            f"    b {field[('C', 1)]}   {field[('E', 2)]}   {field[('G', 2)]}   {field[('I', 1)]} k")
        print(f"      c {field[('D', 1)]}   {field[('F', 2)]}   {field[('H', 1)]} i")
        print(f"        d {field[('E', 1)]}   {field[('G', 1)]} h")
        print(f"          e {field[('F', 1)]} g")
        print(f"            f")


def check_pos_on_field(a_ind, i_ind): # проверяет позицию выбранной фигуры - есть ли такая клетка на доске
    if a_ind == 'A':
        return 1 <= i_ind <= 6
    elif a_ind == 'B':
        return 1 <= i_ind <= 7
    elif a_ind == 'C':
        return 1 <= i_ind <= 8
    elif a_ind == 'D':
        return 1 <= i_ind <= 9
    elif a_ind == 'E':
        return 1 <= i_ind <= 10
    elif a_ind == 'F':
        return 1 <= i_ind <= 11
    elif a_ind == 'L':
        return 1 <= i_ind <= 6
    elif a_ind == 'K':
        return 1 <= i_ind <= 7
    elif a_ind == 'I':
        return 1 <= i_ind <= 8
    elif a_ind == 'H':
        return 1 <= i_ind <= 9
    elif a_ind == 'G':
        return 1 <= i_ind <= 10
