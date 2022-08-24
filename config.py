"""Дополнительный модуль: работа с файлами конфигурации и данных."""

from pathlib import Path
from sys import argv
from configparser import ConfigParser as CP


# глобальные переменные модуля config
SCRIPT_DIR = Path(argv[0]).parent
PLAYERS_INI_PATH = SCRIPT_DIR / "players.ini"
SAVES_INI_PATH = SCRIPT_DIR / "saves.ini"

PLAYERS = ()
STATS = {}
SAVES = {}

# переменные типов для аннотации
#Row = list[str | int | float] | tuple[str | int | float, ...]
#Matrix = tuple[Row, ...] | list[Row]
TurnCoords = tuple[int, int]
Score = tuple[dict, dict]


def read_ini() -> bool:
    """Читает конфигурационные файлы, сохраняет прочитанные данные в глобальные переменные статистики и сохранений и возвращает True если приложение запущено впервые, иначе False."""
    global STATS, SAVES
    # для работы с .ini файлами используем парсер из стандартной библиотеки
    ini_file = CP()
    ini_file.read(PLAYERS_INI_PATH)
    # players.ini -> STATS
    for player in ini_file.sections():
        tr = True if ini_file[player]['training'] == 'True' else False
        st = ini_file[player]['stats'].split(',')
        STATS[player] = {'training': tr, 'stats': {'wins': int(st[0]),
                                                   'ties': int(st[1]),
                                                   'fails': int(st[2])}}
    # необходимо очистить объект ini_file, иначе при последовательном чтении второго файла его поля будут ДОзаписаны в объект ini_file
    ini_file.clear()
    ini_file.read(SAVES_INI_PATH)
    # saves.ini -> SAVES
    for save in ini_file.sections():
        players = frozenset(save.split(','))
        SAVES[players] = dict(ini_file[save])
    # отсутствие сохранённых ранее имён игроков трактуем как первый запуск приложения
    if STATS:
        return False
    else:
        return True


def save_ini():
    """Записывает конфигурационные файлы, из глобальных переменных статистики и сохранений."""
    # STATS -> players.ini
    # SAVES -> saves.ini