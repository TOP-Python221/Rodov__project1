"""Дополнительный модуль: глобальные переменные и константы."""

from pathlib import Path
from sys import argv
from configparser import ConfigParser as CP


# глобальные переменные
SCRIPT_DIR = Path(argv[0]).parent
PLAYERS_INI_PATH = SCRIPT_DIR / "players.ini"
SAVES_INI_PATH = SCRIPT_DIR / "saves.ini"

DIM = 3
RANGE = range(DIM)

TOKENS = ('X', 'O')

# ИСПОЛЬЗОВАТЬ: переменные STATS, SAVES, PLAYERS и PLAYERS должны быть инициализированы пустыми контейнерами — данными они заполняются только во время работы разных функций
# КОММЕНТАРИЙ: если вам необходимо изменить данные для тестирования функций, то это всегда можно сделать из любого другого модуля (см. тест в модуле functions)
STATS = {}
SAVES = {}

BOT_NAME_EASY = 'bot1'
BOT_NAME_HARD = 'bot2'

WEIGHT_OWN = 1.5
WEIGHT_FOE = 1

STRATEGY_MATRICES = ()

PLAYERS = ()

BOARD = [['']*DIM for _ in range(DIM)]


# переменные типов для аннотации
Row = list[str | int | float] | tuple[str | int | float, ...]
Matrix = tuple[Row, ...] | list[Row]
TurnCoords = tuple[int, int]
Score = tuple[dict, dict]


# глобальные константы
APP_TITLE = 'Крестики-Нолики'
PROMPT = ' > '

COMMANDS = {
    'добавить нового игрока': ('player', 'p', 'игрок', 'и'),
    'выбрать другого игрока': ('another', 'a', 'другой', 'д'),
    'начать новую партию': ('game', 'g', 'партия', 'п'),
    'загрузить партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить статистику': ('stats', 's', 'таблица', 'т'),
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'показать справку': ('help', 'h', 'справка', 'с'),
    'включить режим обучения': ('training', 't', 'обучение', 'о'),
    'выйти из игры': ('quit', 'q', 'выход', 'в'),
}


# СДЕЛАТЬ: оставить в данном модуле только объявление глобальных переменных, а все вспомогательные функции общего назначения вынести в модуль functions (бывший commands)

# КОММЕНТАРИЙ: таким образом, в модуле config у нас не будет импортов других дополнительных модулей проекта, а значит не будет и проблем с закольцованным импортом (модули стандартной библиотеки импортировать можно, потому что они не относятся к нашему проекту, с ними закольцованность никогда не возникнет)

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