"""Дополнительный модуль: обработка пользовательских команд и вспомогательные функции общего назначения."""

from shutil import get_terminal_size as gts

import config
import gamemode


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
    width_boards = tuple(width_cells[i]*config.DIM + config.DIM - 1
                         for i in range(num_of_boards))
    pad = 5
    margin = (left_margin, gts()[0] - 1 - sum(width_boards) - pad * (num_of_boards - 1))[right]
    # формирует строки со значениями и вертикальными разделителями
    value_lines = ()
    for i in config.RANGE:
        # записывает в кортеж строки значений из каждой переданной матрицы
        values = ('|'.join(f"{cell!s:^{width_cells[j]}s}" for cell in boards[j][i])
                  for j in range(num_of_boards))
        # формирует полную строку с отступами слева и между строками значений
        value_lines += (' '*margin + (' '*pad).join(values), )
    # формирует строку с горизонтальными разделителями матриц и отступами слева и между ними
    horiz_line = ' '*margin + (' '*pad).join('—'*wd for wd in width_boards)
    return f'\n{horiz_line}\n'.join(value_lines)


def load() -> bool:
    """Выводит в stdout все сохранённые партии для текущего игрока, запрашивает партию для загрузки, настраивает глобальные переменные и возвращает True/False в зависимости от очерёдности хода."""
    # УДАЛИТЬ: разве имя игрока не функция gamemode.get_player_name() запрашивает? разве имя первого игрока на момент вызова этой функции уже не находится в config.PLAYERS?
    name = input('Введите имя игрока: ')
    if name in config.PLAYERS:
        saves_found = False
        for save in config.SAVES:
            # ОТВЕТИТЬ: какая структура переменной config.SAVES? вы ведёте себя с ней совершенно по разному: то там словарь со строковым ключом, то что-то совсем другое — а в Архитектуре вообще frozenset записан в качестве ключа
            if name in save:
                # ОТВЕТИТЬ: здесь вы предлагаете загрузить первую же найденную партию — остальные игнорируете? или вы разрешите только один сейв на игрока?
                choice = input('Хотите загрузить старую партию или начать новую? '
                               '(Введите: Загрузить старую или Начать новую)')
                if choice == 'Загрузить старую':
                    # СДЕЛАТЬ: здесь необходимо получить значения из сейва и соответственно настроить глобальные переменные в config, после чего вернуться в управляющий код
                    pass

                elif choice == 'Начать новую':
                    # УДАЛИТЬ: вызов этой функции — не ответственность функции load()
                    gamemode.game_mode()
                    # КОММЕНТАРИЙ: если вы хотите предоставить игроку во время загрузки возможность отказаться от загрузки, то надо вернуться из этой функции в суперцикл main с определённым значением, которое подскажет управляющему коду, что нужно перейти на следующую итерацию суперцикла и ждать новую команду
            # save -> stdout
            saves_found = True
    # if not saves_found:
    #     raise LookupError
    # stdin -> choice
    # config.SAVES[choice]['turns'] -> game.BOARD
    # choice -> gameset.PLAYERS
    # if turns_amount % 2 == 0:
    #     return False
    # else:
    #     return True


def change_dimension(new_dimension: int = None) -> None:
    """Запрашивает у пользователя новую размерность игрового поля и пересчитывает соответствующий диапазон."""
    if not new_dimension:
        while True:
            new_dimension = input('Введите новый размер поля (одно целое число): ')
            if new_dimension.isdecimal():
                new_dimension = int(new_dimension)
                break
    config.DIM = new_dimension
    config.RANGE = range(new_dimension)
    config.BOARD = [['']*new_dimension for _ in config.RANGE]


def is_first_game() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""
    for config.PLAYERS[0] in config.PLAYERS:
        # ИСПРАВИТЬ: не знаю, какую цель вы здесь преследуете, но как строковый литерал может быть явно равен константе логического типа?
        if config.STATS[config.PLAYERS[0]]['training' == True]:
            return True
    else:
        return False


# тесты
if __name__ == '__main__':
    change_dimension(11)
    config.BOARD = [[f'{i+1} {j+1}' for j in config.RANGE] for i in config.RANGE]
    print(draw_boards(config.BOARD))
