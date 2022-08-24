"""Дополнительный модуль: раздел помощи и режим обучения."""

from shutil import get_terminal_size as gts
from math import ceil, floor

import gameset
import game


# глобальные переменные модуля help
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

H_RULES = f"""Правила игры
    Вы играете одним из двух символов: крестиком {gameset.TOKENS[0]!r} или ноликом {gameset.TOKENS[1]!r}. Чтобы победить, первым составьте последовательность из {gameset.DIM} своих символов в одной строке, в одном столбце, либо в одной диагонали.
"""
BOARD_COORDINATES = [[f'{i + 1} {j + 1}' for j in gameset.RANGE] for i in gameset.RANGE]
H_INTERFACE = f"""Интерфейс
    Игра предлагает вам интерфейс командной строки. Это означает, что для выполнения определённого действия в игре необходимо ввести команду и нажать Enter. В последнем разделе данной справки приведён список действий и соответствующих им команд, которые можно использовать в главном меню между партиями.
    
    Во время выполнения различных действий игра может запрашивать у вас дополнительные данные или задавать уточняющие вопросы. В таких случаях возможные варианты ввода перечисляются в скобках в конце строки с приглашением для ввода. Отсутствие перечисления вариантов ввода означает, что можно вводить любые данные: например, когда игра запрашивает имя игрока.  
    
    Во время партии игра ожидает от игрока(-ов) ввода координат клетки для текущего хода. Координаты вводятся через пробел в соответствии с примером ниже. Ввод пустой строки во время своего хода позволит вам сохранить незавершённую партию и вернуться в главное меню.
\n{game.draw_boards(BOARD_COORDINATES, left_margin=6)}\n"""
H_COMMANDS = (
    "Команды\n"
    # формирует строку в виде таблицы, колонки разделяются двоеточиями, первая колонка выравнивается вправо, вторая колонка выравнивается влево, первая строка отделяется горизонтальной линией
    + ' '*(4 + (mx_com_len := max(len(k) for k in COMMANDS)) - len(a := 'действие'))
    + a.title() + ": 'команда 1', 'команда 2', ...\n  "
    + '—'*(4 + mx_com_len + max(len(str(v)) for v in COMMANDS.values())) + '\n'
    + '\n'.join(' '*(4 + mx_com_len - len(com))
                + com.capitalize() + ": "
                + ', '.join(repr(o) for o in opt)
                for com, opt in COMMANDS.items()) + '\n\n'
)


def show_help() -> None:
    """Выводит в stdout раздел помощи."""
    # из глобального пространства имён данного модуля получает все объекты, чьи имена начинаются на 'H_'
    for chapter in (obj for name, obj in globals().items() if name.startswith('H_')):
        title, message = (ch := chapter.split('\n', maxsplit=1))[0], ch[1]
        show_title(title, center=False)
        print(message)


def show_title(title: str, *,
               padding_vertical: bool = False,
               center: bool = True,
               uppercase: bool = True) -> None:
    """Выводит в stdout заголовок в рамке."""
    terminal_width = gts()[0] - 1
    if center:
        # отступы при центрировании для чётного и нечётного значений ширины окна терминала
        padding_left = ceil((terminal_width - len(title) - 2) / 2)
        padding_right = floor((terminal_width - len(title) - 2) / 2)
    else:
        padding_left = 1
        padding_right = terminal_width - len(title) - padding_left - 2
    title = (title.capitalize(), title.upper())[uppercase]
    frame_char = ('+', '#')[padding_vertical]
    empty_line = (' '*(terminal_width - 2)).join(frame_char*2) + '\n'
    print(f'\n{frame_char*terminal_width}')
    print(('', empty_line)[padding_vertical], end='')
    print((' '*padding_left + title + ' '*padding_right).join(frame_char*2))
    print(('', empty_line)[padding_vertical], end='')
    print(f'{frame_char*terminal_width}\n')
