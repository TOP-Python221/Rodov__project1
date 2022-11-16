"""Дополнительный модуль: обработка игрового процесса."""

import config
import ai


def human_turn():
    """Запрос координат ячейки поля для текущего хода."""


def bot_turn() -> config.TurnCoords:
    """Возвращает координаты ячейки поля для текущего хода бота в зависимости от сложности."""
    if config.BOT_NAME_EASY in config.PLAYERS:
        return ai.easy_mode()
    elif config.BOT_NAME_HARD in config.PLAYERS:
        return ai.hard_mode(config.PLAYERS.index(config.BOT_NAME_HARD))


def check_win_or_tie() -> bool:
    """Проверяет текущую партию на наличие победной комбинации или ничьей."""
    # нет пустых  победа  ничья
    #   False     False   False
    #   False     True    False
    #   True      False   True
    #   True      True    False


def game(zero_turn=False) -> config.Score | None:
    """Обрабатывает игровой процесс."""
    # config.STRATEGY_MATRICES = (
    #     ai.calc_sm_cross(),
    #     ai.calc_sm_zero()
    # )
    # training = functions.is_first_game()
    # for name in config.PLAYERS:
    #     if zero_turn:
    #         continue
    #     if name in (config.BOT_NAME_EASY, config.BOT_NAME_HARD):
    #         if training:
    #             'подсказка' -> stdout
    #         bot_turn() -> BOARD
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
    #     score[i] -> config.STATS[config.PLAYERS[i]]


def save_game() -> None:
    """Обновляет глобальную переменную сохранений в соответствии с текущим состоянием глобальных переменных текущих игроков и сделанных ходов."""
    # config.PLAYERS, BOARD -> config.SAVES
