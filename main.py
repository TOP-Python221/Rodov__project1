"""Модуль верхнего уровня для учебного проекта 1: Крестики-Нолики."""

# импорт дополнительных модулей проекта
import config
import help
import commands
import gameset
import game


help.show_title(help.APP_TITLE, padding_vertical=True)

# начало отработки Этапов работы приложения согласно Архитектуре

# 1. Загрузка файлов настроек
if config.read_ini():
    # 2. ЕСЛИ первый запуск приложения:
    #         вывод раздела помощи
    help.show_help()

# 3. Запрос имени игрока
gameset.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода пользовательских команд
    command = input(help.PROMPT).lower()

    if command in help.COMMANDS['выйти из игры']:
        break

    elif command in help.COMMANDS['начать новую партию']:
        # 5. Запрос режима игры
        #    6. Запрос символа для игры
        gameset.game_mode()
        # 8. Партия
        #    7. ЕСЛИ первая партия для любого из игроков
        result = game.game()
        if result is None:
            # 9. ЕСЛИ партия закончена досрочно:
            #         сохранение данных о партии
            game.save_game()
        else:
            # 10. Внесение изменений в статистику игрока(-ов)
            game.update_stats(result)

    elif command in help.COMMANDS['загрузить партию']:
        try:
            # 5. Проверка наличия сохранённых партий для текущего игрока
            #    6. Запрос партии для загрузки
            # 7. Партия
            result = game.game(commands.load())
            if result is None:
                # 8. ЕСЛИ партия закончена досрочно:
                #         сохранение данных о партии
                game.save_game()
            else:
                # 9. Внесение изменений в статистику игрока(-ов)
                game.update_stats(result)
                # 10. Удаление данных о доигранной сохранённой партии
                # ...
        except LookupError:
            print('no saved games for you')
    elif command in help.COMMANDS['загрузить партию']:
        pass
    # Запрос символа для игры
    token = input('Введите символ, которым будете играть (X или O): ')
    if token == gameset.TOKENS[1]:
        config.SAVES.PLAYERS[0]['tokens'] = token
    else:
        config.SAVES.PLAYERS[0]['tokens'] = 'O'

    # elif ... прочие команды

config.save_ini()
