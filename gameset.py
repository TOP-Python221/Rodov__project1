"""Дополнительный модуль: подготовка игрового процесса."""
import config
# глобальные переменные модуля gameset
DIM = 3
RANGE = range(DIM)

TOKENS = ('X', 'O')
TURNS = [ ['X', 'O', 'O'],
          ['X', 'X', ' '],
          [' ', 'O', ' '] ]

"""Запрос имени игрока и передача введённого значения в глобальную переменную STATS"""
def get_player_name(name) -> None:
    """Объявление глобальной переменной STATS в локальной функций get_player_name"""
    """Запрашивает имя игрока. """
    while True:
        player_name = input('Введите имя пользователя: ')
        if player_name:
            break
        else:
            print('Введите не пустую строку!')
    """И проверяет присутствие этого имени в глобальной переменной статистики."""
    if player_name not in config.STATS:
        """Создаёт запись о новом игроке в глобальной переменной статистики."""
        config.STATS[player_name] = {'training': True,
                     'stats': {'wins': 0, 'ties': 0, 'fails': 0}}
    config.PLAYERS.append(player_name)


def game_mode() -> str:
    """Запрашивает режим для новой партии, добавляет имя бота либо второго игрока в глобальную переменную текущих игроков, запрашивает очерёдность ходов."""
    # stdin -> mode
    # if mode == 'single':
    mode = input('Введите режим игры (single - с ботом или double - с другим пользователем): ')
    if mode == 'single':
        game_mode.get_difficultly_level()
    elif mode == 'double':
        get_player_name()
    # stdin -> who_is_cross
    config.PLAYERS.append(name)
    return mode
    # name -> PLAYERS
    # return -> mode


def is_first_game() -> bool:
    """Проверяет является ли данная партия первой для любого из игроков."""
    for config.PLAYERS[0] in config.PLAYERS:
        if config.STATS[config.PLAYERS[0]]['training' == True]:
            return True
    else:
        return False