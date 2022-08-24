"""Дополнительный модуль: подготовка игрового процесса."""

# глобальные переменные модуля gameset
DIM = 3
RANGE = range(DIM)

TOKENS = ('X', 'O')
TURNS = [ ['X', 'O', 'O'],
          ['X', 'X', ' '],
          [' ', 'O', ' '] ]

def get_player_name() -> None:
    """Запрашивает имя игрока и проверяет присутствие этого имени в глобальной переменной статистики, добавляет имя в глобальную переменную текущих игроков."""
    # stdin -> name
    # if name not in config.STATS:
    #     new_player(name)
    # name -> PLAYERS


def game_mode() -> str:
    """Запрашивает режим для новой партии, добавляет имя бота либо второго игрока в глобальную переменную текущих игроков, запрашивает очерёдность ходов."""
    # stdin -> mode
    # if mode == 'single':
    #     get_difficulty_level()
    # elif mode == 'double':
    #     get_player_name()
    # stdin -> who_is_cross
    # name -> PLAYERS
    # return -> mode


def is_first_game() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""
    # for name in PLAYERS:
    #     if config.STATS[name]['training']:
    #         return True
    # else:
    #     return False