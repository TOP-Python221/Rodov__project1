"""Дополнительный модуль: искусственный интеллект."""

import config
import gameset
import game


# глобальные переменные модуля ai
BOT_NAME_EASY = 'bot1'
BOT_NAME_HARD = 'bot2'

WEIGHT_OWN = 1.5
WEIGHT_FOE = 1

SM_FROM_CENTER = []
SM_FROM_CORNERS = []


def bot_turn() -> config.TurnCoords:
    """Возвращает координаты ячейки поля для текущего хода бота в зависимости от сложности."""
    if BOT_NAME_EASY in gameset.PLAYERS:
        return easy_mode()
    elif BOT_NAME_HARD in gameset.PLAYERS:
        return hard_mode(gameset.PLAYERS.index(BOT_NAME_HARD))


def easy_mode() -> config.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода бота для низкого уровня сложности."""


def hard_mode(token_index: int) -> config.TurnCoords:
    """Рассчитывает координат ячейки поля для текущего хода для высокого уровня сложности."""


def cells_row(matrix: config.Matrix, row_index: int) -> tuple:
    """Возвращает кортеж с элементами ряда матрицы по индексу ряда."""
    return tuple(matrix[row_index])


def cells_column(matrix: config.Matrix, column_index: int) -> tuple:
    """Возвращает кортеж с элементами столбца матрицы по индексу столбца."""
    return tuple(matrix[i][column_index] for i in gameset.RANGE)


def cells_maindiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами главной диагонали матрицы по индексам ряда и столбца."""
    if row_index == column_index:
        return tuple(matrix[i][i] for i in gameset.RANGE)
    else:
        return tuple()


def cells_antidiagonal(matrix: config.Matrix, row_index: int, column_index: int) -> tuple:
    """Возвращает кортеж с элементами побочной диагонали матрицы по индексам ряда и столбца."""
    if row_index == gameset.DIM - column_index - 1:
        return tuple(matrix[i][gameset.DIM - i - 1] for i in gameset.RANGE)
    else:
        return tuple()


def sum_matrix(*matrices: config.Matrix) -> config.Matrix:
    """Поэлементно складывает переданные матрицы и возвращает результирующую матрицу."""
    result_matrix = []
    for i in gameset.RANGE:
        result_matrix += [[]]
        for j in gameset.RANGE:
            result_matrix[i] += [sum(matrix[i][j] for matrix in matrices)]
    return result_matrix


def indexes_matrix_max(matrix: config.Matrix) -> config.TurnCoords:
    """Находит наибольший элемент в матрице и возвращает индексы этого элемента в виде кортежа."""
    mx, coords = 0, ()
    for i in gameset.RANGE:
        for j in gameset.RANGE:
            if mx < matrix[i][j]:
                mx, coords = matrix[i][j], (i, j)
    return coords


def weights_tokens(board: config.Matrix, token_index: int) -> config.Matrix:
    """Конструирует и возвращает матрицу весов занятых ячеек игрового поля."""
    tokens_weights = [[0]*gameset.DIM for _ in gameset.RANGE]
    for i in gameset.RANGE:
        for j in gameset.RANGE:
            if board[i][j] == gameset.TOKENS[token_index]:
                tokens_weights[i][j] = WEIGHT_OWN
            elif board[i][j] == gameset.TOKENS[1 - token_index]:
                tokens_weights[i][j] = WEIGHT_FOE
    return tokens_weights


def weights_empty(tokens_weights: config.Matrix) -> config.Matrix:
    """Вычисляет и возвращает матрицу весов пустых ячеек игрового поля."""
    empty_weights = [[0]*gameset.DIM for _ in gameset.RANGE]
    for i in gameset.RANGE:
        for j in gameset.RANGE:
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
    resolve_weights = [[0]*gameset.DIM for _ in gameset.RANGE]
    for i in gameset.RANGE:
        for j in gameset.RANGE:
            if not game.BOARD[i][j]:
                resolve_weights[i][j] = empty_weights[i][j]
    return resolve_weights


def calc_strategy_matrices() -> None:
    """Вычисляет и заполняет начальные матрицы принятия решений для стратегий 'крестика' и 'нолика'.
    ВНИМАНИЕ: вычисляет корректные матрицы только для нечётных значений размерности игрового поля (gameset.DIM)."""
    global SM_FROM_CENTER, SM_FROM_CORNERS
    SM_FROM_CENTER = [[0] * gameset.DIM for _ in gameset.RANGE]
    from_center_weights = (tuple(range(gameset.DIM // 2, 0, -1))
                           + (gameset.DIM // 2 + 1,)
                           + tuple(range(1, gameset.DIM // 2 + 1)))
    for i in gameset.RANGE:
        SM_FROM_CENTER[i][i] = from_center_weights[i]
        SM_FROM_CENTER[i][gameset.DIM - i - 1] = from_center_weights[i]

    SM_FROM_CORNERS = [[0] * gameset.DIM for _ in gameset.RANGE]
    from_corners_weights = (tuple(range(gameset.DIM // 2 + 1, 1, -1))
                            + tuple(range(1, gameset.DIM // 2 + 2)))
    for j in (0, gameset.DIM-1):
        SM_FROM_CORNERS[j] = list(from_corners_weights)
        SM_FROM_CORNERS[j] = list(from_corners_weights)
        for i in gameset.RANGE:
            SM_FROM_CORNERS[i][j] = from_corners_weights[i]
    
