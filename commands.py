"""Дополнительный модуль: обработка пользовательских команд."""

import config
import gameset
import game





def load() -> bool:
    """Выводит в stdout все сохранённые партии для текущего игрока, запрашивает партию для загрузки, настраивает глобальные переменные и возвращает True/False в зависимости от очерёдности хода."""

    name = input('Введите имя игрока: ')
    if name in config.PLAYERS:
        saves_found = False
        for save in config.SAVES:
            if name in save:
                choice = input('Хотите загрузить старую партию или начать новую? '
                               '(Введите: Загрузить старую или Начать новую)')
                if choice == 'Загрузить старую':
                    pass
                elif choice == 'Начать новую':
                    gameset.game_mode()
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


def change_dimension() -> None:
    """Запрашивает у пользователя новую размерность игрового поля и пересчитывает соответствующий диапазон."""
    # stdin -> gameset.DIM
    # gameset.DIM -> gameset.RANGE