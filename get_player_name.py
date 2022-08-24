"""Импорт из модуля main глобальной переменной STATS"""
import config

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
