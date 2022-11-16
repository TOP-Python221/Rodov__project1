"""Дополнительный модуль: подготовка игрового процесса."""

import config
bot_name = 'Andrey' # Данная переменная была добавлена, чтобы интерпретатор не ругался на её отсутствие :)


def game_mode():
    """Запрашивает режим для новой партии, добавляет имя бота либо второго игрока в глобальную переменную текущих игроков, запрашивает очерёдность ходов."""
    mode = input('Введите режим игры (single - с ботом или double - с другим пользователем): ')
    if mode.lower() == 'single':
        get_difficultly_level()
    elif mode.lower() == 'double':
        get_player_name()
        #config.PLAYERS += (name, )


def get_player_name() -> None:
    """Запрашивает имя игрока, проводит валидацию и, при необходимости, добавляет новый элемент в config.STATS"""
    while True:
        player_name = input('Введите имя пользователя: ')
        # ДОБАВИТЬ: проверку на неравенство введённого имени именам ботов
        if player_name and player_name != bot_name:
            break
        else:
            raise ValueError('Введите корректное значение!')
    # КОММЕНТАРИЙ: далее всё хорошо
    # проверяет присутствие этого имени в config.STATS
    if player_name not in config.STATS:
        # создаёт запись о новом игроке в config.STATS
        config.STATS[player_name] = {'training': True,
                                     'stats': {'wins': 0, 'ties': 0, 'fails': 0}}
    config.PLAYERS += (player_name, )


def get_difficultly_level():
    """Запрашивает у пользователя уровень сложности для игры с ботом."""
    while True:
        level = input('Введите предпочитаемую сложность игры("Легкий или сложный"): ')
        if level == 'легкий':
            config.PLAYERS += (bot_name,) # Добавляет имя бота в список игроков данной партий.
            break
        elif level == 'сложный':
            config.PLAYERS += (bot_name,)
            break




# КОММЕНТАРИЙ:
#  в двойные кавычки мы помещаем строки документации — это строковые литералы, вычисляемые интерпретатором;
#  комментарии мы пишем после символа # — это текст полностью игнорируемый интерпретатором;
#  не путайте больше эти два явления


# КОММЕНТАРИЙ: все тесты убираются под проверку имени модуля, чтобы они не выполнялись, когда данный модуль импортируется
# тесты
if __name__ == '__main__':
    game_mode()