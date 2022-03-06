import random


class Sudoku:
    def __init__(self, matriz):
        self.matriz = matriz
        self.dimension = len(matriz)

    def solve(self):

        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.matriz[i][j] != -1:
                    continue
                else:
                    for v in range(1, 10):
                        if self.is_posible_insert(i, j, v):
                            self.matriz[i][j] = v
                            resp = self.solve()
                            if resp:
                                return True
                            self.matriz[i][j] = -1


                    return False

        print("Solucion encontrada")
        print_matriz(self.matriz)

    def is_posible_insert(self, x, j, value):
        # Recorrer la fila y verificar que no haya un numero igual
        if value in self.matriz[x]:
            return False

        # Recorrer la columna y verificar que no haya un numero igual
        for row in self.matriz:
            if row[j] == value:
                return False

        # Recorrer el cuadrante 3x3 y verificar que no haya un nuemero igual
        row_start = x // 3 * 3
        for row in self.matriz[row_start: row_start + 3]:
            col_start = j // 3 * 3
            for cell in row[col_start: col_start + 3]:
                if cell == value:
                    return False
        return True




def print_matriz(matriz):
    for row in matriz:
        print(row)

def play(test = False):
    matriz = [
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],

        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],

        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1]
    ]
    if test:
        matrix = create_test_sudoku()
        print_matriz(matrix)
    else:
        print("\n----- Welcome to sudoku game resolver -----" )
        print("To create a new sudoku challenge yo need to put in the default values on each position of the matriz")
        print_matriz(matriz)
        print("For this enter ROW,COL,VALUE data. Example: 7,5,9")
        print("Or press ENTER to let the program do his magic. ☺")

        while True:
            user_input = get_user_input()
            if user_input is "":
                break
            [x, y, value] = user_input.replace(' ', '').split(',')
            n_x = int(x)
            n_y = int(y)
            n_v = int(value)
            if 0 < n_x > 9 or 0 < n_y > 9:
                print("Invalid position. Pick a position where 0 <= ROW <= 9 and 0 <= COL <= 9")
                continue
            if not 0 < n_v < 10:
                print("Invalid VALUE. Pick a value where 1 <= VALUE <= 9")
                continue
            matriz[n_x][n_y] = n_v
            print_matriz(matriz)

    sudoku = Sudoku(matriz)
    sudoku.solve()

def get_user_input():
    user_input = input("Enter: ROW,COL,VALUE: ")
    return user_input


def create_test_sudoku():
    m1 = [
        [ 8,  1, -1,   -1, -1, -1,   -1,  2,  9],
        [-1,  4, -1,   -1,  8, -1,   -1,  1, -1],
        [-1, -1, -1,    5,  3,  1,   -1, -1, -1],

        [-1, -1,  1,   -1,  6, -1,    2, -1, -1],
        [-1,  8,  6,   -1,  2, -1,    1,  9, -1],
        [-1, -1,  4,   -1,  9, -1,    3, -1, -1],

        [-1, -1, -1,    3,  5,  9,   -1, -1, -1],
        [-1,  6, -1,   -1,  7, -1,   -1,  3, -1],
        [ 3,  7, -1,   -1, -1, -1,   -1,  5,  4]
    ]
    # m2 = [
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    # ]
    # m3 = [
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    # ]
    # m4 = [
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    # ]
    # m5 = [
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
    #     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    # ]
    # sudoku_list_test = list(m1, m2, m3, m4, m5)
    # return random.choice(sudoku_list_test)
    return m1


if __name__ == '__main__':
    play(True)


