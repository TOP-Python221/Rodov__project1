"""Дополнительный модуль: обработка игрового процесса."""

from shutil import get_terminal_size as gts

import config
import gameset
import ai


# глобальные переменные модуля game
BOARD = [[''] * gameset.DIM for _ in range(gameset.DIM)]


def draw_boards(board: config.Matrix,
                *boards: config.Matrix,
                left_margin: int = 1,
                right: bool = False) -> str:
    """Возвращает в строковом виде одно или несколько игровых полей, расположенных на одном уровне, заполненных на основе переданных аргументами матриц."""
    boards = (board, ) + boards
    num_of_boards = len(boards)
    # для каждой матрицы вычисляет наибольшее количество символов в ячейке
    width_cells = tuple(max(max(len(str(cell)) for cell in row) for row in board) + 2
                        for board in boards)
    # для каждой матрицы вычисляет количество символов, занимаемое всей матрицей в ширину
    width_boards = tuple(width_cells[i]*gameset.DIM + gameset.DIM - 1
                         for i in range(num_of_boards))
    pad = 5
    margin = (left_margin, gts()[0] - 1 - sum(width_boards) - pad * (num_of_boards - 1))[right]
    # формирует строки со значениями и вертикальными разделителями
    value_lines = ()
    for i in gameset.RANGE:
        # записывает в кортеж строки значений из каждой переданной матрицы
        values = ('|'.join(f"{cell!s:^{width_cells[j]}s}" for cell in boards[j][i])
                  for j in range(num_of_boards))
        # формирует полную строку с отступами слева и между строками значений
        value_lines += (' '*margin + (' '*pad).join(values), )
    # формирует строку с горизонтальными разделителями матриц и отступами слева и между ними
    horiz_line = ' '*margin + (' '*pad).join('—'*wd for wd in width_boards)
    return f'\n{horiz_line}\n'.join(value_lines)


def human_turn():
    """Запрос координат ячейки поля для текущего хода."""


def game(zero_turn=False) -> config.Score | None:
    """Обрабатывает игровой процесс."""
    #ai.calc_strategy_matrices()
    #training = is_first_game()
    # for name in gameset.PLAYERS:
    #     if zero_turn:
    #         continue
    #     if name in (ai.BOT_NAME_EASY, ai.BOT_NAME_HARD):
    #         if training:
    #             'подсказка' -> stdout
    #         ai.bot_turn() -> BOARD
    #     else:
    #         human_turn() -> inp
    #         if inp:
    #             inp -> BOARD
    #         else:
    #             return None
    #     check_win_or_tie() -> win_or_tie
    #     if win_or_tie ...:
    #         return -> ({}, {})


def update_stats(score: config.Score) -> None:
    """Обновляет глобальную переменную статистики в соответствии с результатом завершённой партии."""
    # for i in range(2):
    #     score[i] -> config.STATS[gameset.PLAYERS[i]]


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # gameset.PLAYERS, BOARD -> config.SAVES
