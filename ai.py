"""Дополнительный модуль: искусственный интеллект."""

import config
import functions


def easy_mode() -> config.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода бота для низкого уровня сложности."""


def hard_mode(token_index: int) -> config.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода для высокого уровня сложности."""


def cells_row(matrix: config.Matrix, row_index: int) -> tuple:
    """Возвращает кортеж с элементами ряда матрицы по индексу ряда."""
    return tuple(matrix[row_index])


def cells_column(matrix: config.Matrix, column_index: int) -> tuple:
    """Возвращает кортеж с элементами столбца матрицы по индексу столбца."""
    return tuple(matrix[i][column_index] for i in config.RANGE)


def cells_maindiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами главной диагонали матрицы по индексам ряда и столбца."""
    if row_index == column_index:
        return tuple(matrix[i][i] for i in config.RANGE)
    else:
        return tuple()


def cells_antidiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами побочной диагонали матрицы по индексам ряда и столбца."""
    if row_index == config.DIM - column_index - 1:
        return tuple(matrix[i][config.DIM - i - 1] for i in config.RANGE)
    else:
        return tuple()


def sum_matrix(*matrices: config.Matrix) -> config.Matrix:
    """Поэлементно складывает переданные матрицы и возвращает результирующую матрицу."""
    result_matrix = []
    for i in config.RANGE:
        result_matrix += [[]]
        for j in config.RANGE:
            result_matrix[i] += [sum(matrix[i][j] for matrix in matrices)]
    return result_matrix


def indexes_matrix_max(matrix: config.Matrix) -> config.TurnCoords:
    """Находит наибольший элемент в матрице и возвращает индексы этого элемента в виде кортежа."""
    mx, coords = 0, ()
    for i in config.RANGE:
        for j in config.RANGE:
            if mx < matrix[i][j]:
                mx, coords = matrix[i][j], (i, j)
    return coords


def weights_tokens(board: config.Matrix, token_index: int) -> config.Matrix:
    """Конструирует и возвращает матрицу весов занятых ячеек игрового поля."""
    tokens_weights = [[0]*config.DIM for _ in config.RANGE]
    for i in config.RANGE:
        for j in config.RANGE:
            if board[i][j] == config.TOKENS[token_index]:
                tokens_weights[i][j] = config.WEIGHT_OWN
            elif board[i][j] == config.TOKENS[1 - token_index]:
                tokens_weights[i][j] = config.WEIGHT_FOE
    return tokens_weights


def weights_empty(tokens_weights: config.Matrix) -> config.Matrix:
    """Вычисляет и возвращает матрицу весов пустых ячеек игрового поля."""
    empty_weights = [[0]*config.DIM for _ in config.RANGE]
    for i in config.RANGE:
        for j in config.RANGE:
            if tokens_weights[i][j] == 0:
                r = cells_row(tokens_weights, i)
                if len(set(r) - {0}) == 1:
                    empty_weights[i][j] += int(sum(r)**2)
                c = cells_column(tokens_weights, j)
                if len(set(c) - {0}) == 1:
                    empty_weights[i][j] += int(sum(c)**2)
                md = cells_maindiagonal(tokens_weights, i, j)
                if len(set(md) - {0}) == 1:
                    empty_weights[i][j] += int(sum(md)**2)
                ad = cells_antidiagonal(tokens_weights, i, j)
                if len(set(ad) - {0}) == 1:
                    empty_weights[i][j] += int(sum(ad)**2)
    return empty_weights


def weights_clear(empty_weights: config.Matrix) -> config.Matrix:
    """Обрабатывает матрицу принятия решения, приравнивая к нолю элементы, соответствующие занятым на поле клеткам."""
    resolve_weights = [[0]*config.DIM for _ in config.RANGE]
    for i in config.RANGE:
        for j in config.RANGE:
            if not config.BOARD[i][j]:
                resolve_weights[i][j] = empty_weights[i][j]
    return resolve_weights


def calc_sm_cross() -> config.Matrix:
    """Вычисляет и возвращает начальную матрицу стратегии крестика."""
    sm_cross = [[0]*config.DIM for _ in config.RANGE]
    half, rem = divmod(config.DIM, 2)
    diag = list(range(1, half+1)) + list(range(half+rem, 0, -1))
    for i in config.RANGE:
        sm_cross[i][i] = diag[i]
        sm_cross[i][-i-1] = diag[i]
    return sm_cross


def calc_sm_zero() -> config.Matrix:
    """Вычисляет и возвращает начальную матрицу стратегии нолика."""

    def triangle_desc(n: int, start: int) -> config.Matrix:
        """Генерирует и возвращает верхне-треугольную по побочной диагонали матрицу, заполняемую параллельно побочной диагонали значениями по убыванию."""
        flat = []
        indexes = range(n)
        for i in indexes:
            flat += [m if m > 0 else 0 for m in range(start-i, -start, -1)][:n]
        matrix = [flat[i*n:(i+1)*n] for i in indexes]
        if n > 2:
            for i in indexes:
                for j in indexes:
                    if i > n-j-1:
                        matrix[i][j] = 0
        return matrix

    def rot90(matrix: config.Matrix) -> config.Matrix:
        """Возвращает "повёрнутую" на 90° матрицу."""
        indexes = range(len(matrix))
        matrix = [[matrix[j][i] for j in indexes] for i in indexes]
        for i in indexes:
            matrix[i] = matrix[i][::-1]
        return matrix

    half, rem = divmod(config.DIM, 2)
    quarter = triangle_desc(half, half+rem)
    if config.DIM > 6:
        for i in range(half):
            for j in range(half):
                if i == half-j-1:
                    if i != j:
                        quarter[i][j] -= 1
                if i > half-j:
                    quarter[i][i] = half - i - (rem+1)%2
    m1 = quarter
    m2 = rot90(m1)
    m3 = rot90(m2)
    m4 = rot90(m3)
    top, bot = [], []
    for i in range(half):
        top += [m1[i] + [0]*rem + m2[i]]
        bot += [m4[i] + [0]*rem + m3[i]]
    return top + [[0]*config.DIM]*rem + bot


# тесты
if __name__ == '__main__':
    functions.change_dimension(7)
    smc = calc_sm_cross()
    smz = calc_sm_zero()
    print(functions.draw_boards(smc, smz))
