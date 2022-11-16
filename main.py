"""Модуль верхнего уровня для учебного проекта 1: Крестики-Нолики."""

# импорт дополнительных модулей проекта
import config
import functions
import help
import gamemode
import game


help.show_title(config.APP_TITLE, padding_vertical=True)

# начало отработки Этапов работы приложения согласно Архитектуре

# 1. Загрузка файлов настроек
if config.read_ini():
    # 2. ЕСЛИ первый запуск приложения:
    #         вывод раздела помощи
    help.show_help()

# 3. Запрос имени игрока
gamemode.get_player_name()

# суперцикл
while True:
    # 4. Ожидание ввода пользовательских команд
    command = input(config.PROMPT).lower()

    if command in config.COMMANDS['выйти из игры']:
        break

    elif command in config.COMMANDS['начать новую партию']:
        # 5. Запрос режима игры
        #    6. Запрос символа для игры
        gamemode.game_mode()
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
        # Если первая партия для любого из игроков - режим обучения
        if functions.is_first_game() is True:
            print(help.H_RULES)

    elif command in config.COMMANDS['загрузить партию']:
        try:
            # 5. Проверка наличия сохранённых партий для текущего игрока
            #    6. Запрос партии для загрузки
            # 7. Партия
            result = game.game(functions.load())
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

    elif command in config.COMMANDS['загрузить партию']:
        pass

    elif command in config.COMMANDS['выйти из игры']:
        # УДАЛИТЬ: этот код должен находиться в функции save_ini()
        # ИСПРАВИТЬ: если вы читаете весь файл в переменную, потом вносите в неё изменения, а потом ДОзаписываете информацию в файл, то в файле у вас будет иметь место дублирование информации
        file = open('saves.ini', 'a+', encoding='utf-8')
        file.write(config.SAVES)
        file.close()

    # elif ... прочие команды


    # СДЕЛАТЬ: этот код должен быть в функции, которая должна находиться в модуле functions
    # Запрос символа для игры
    token = input('Введите символ, которым будете играть (X или O): ')
    if token == config.TOKENS[1]:
        # ИСПРАВИТЬ: какая у вас структура переменной config.SAVES?
        config.SAVES.PLAYERS[0]['tokens'] = token
    else:
        config.SAVES.PLAYERS[1]['tokens'] = 'O'


config.save_ini()
