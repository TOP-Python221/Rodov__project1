from gameset import TURNS

def show_field() -> str:
    """Используемые переменные для работы с функцией"""
    global TURNS
    O_turns = []
    X_turns = []
    counter = 1

    """Выводит в консоль игровое поле"""
    # Добавляет вертикальные линии
    vertical_line = '|'.join([' '*3]*3)
    # Добавляет горизонтальные линии
    horiz_line = '|'.join(['—'*3]*3)
    # Перебор длины вертикальных линий
    for i in range(len(vertical_line)):
        if i > 1:
            break
        else:
            pass
            #print(vertical_line, horiz_line, sep='\n')
            #print(vertical_line)

        # Здесь я пытался записывать координаты в переменные(X_turns, O_turns = [])

        # Из-за того, что нумерация индекса идёт с 0, был добавлен счётчик. А так же, он ещё должен использоваться
        #   для выявления координат второй и третьей горизонтальной линий. То бишь, индексы элементов всех трёх линий - 0, 1,
        #       2. И когда итерация доходит до первого уровня второй линий, то к индексам элементов второго уровня
        #           прибавлялось число 3 и к индексам третьей линий цифра 6, соответственно. Должно было получится
        #               что-то наподобие этого:
        #
        #[ ['X', 'O', 'O'],   [ ['1', '2', '3'],
        #  ['X', 'X', ' '],     ['4', '5', ' '],
        #  [' ', 'O', ' '] ]    [' ', '8', ' '] ]
        #
        #   X_turns = [1, 4, 5]
        #   O_turns = [2, 3, 8]
        #
    for i in range(len(TURNS)):
        if counter <= 3:
            print(f'Первый уровень: {TURNS[i]}')
            for j in range(len(TURNS[i])):
                print(f'Второй уровень: {TURNS[i][j]}')
                if TURNS[i][j] == 'X':
                    for index in enumerate(TURNS[i][j]):
                        X_turns.append(index[0] + counter)
                        print(f'Координаты Х: {X_turns}')
                elif TURNS[i][j] == 'O':
                    for index in enumerate(TURNS[i][j]):
                        X_turns.append(index[0] + counter)
                        print(f'Координаты O: {O_turns}')
                    counter += 1
                else:
                    continue


    print(f'Итог: {O_turns, X_turns}')
    # СДЕЛАТЬ: няшненько.
    #          а теперь загляните в документ Архитектура, в раздел 4. Работа с данными в приложении, подраздел # Ходы в текущей партии: в нём описана структура данных, в которую записываются все ходы - именно из этой структуры вам необходимо извлечь данные о сделанных ходах и вывести их в stdout - и сделать это должна данная функция


#show_field()

"""Черновые наработки :)"""
#for index, value in enumerate(TURNS):
       # print(f'Индексы первого уровня: {list(str(index + 1))}', '\n', type(list(str(index + 1)))')
        #if index in enumerate(TURNS) == ['1']:
            #for k in range(len(TURNS)):
                #for index in enumerate(TURNS[k]):
                    #print(f'Координаты: {list(str(index))}')


                #if TURNS[i][j] == 'X':
                    #X_turns.append(TURNS[i][j])
                #elif TURNS[i][j] == 'O':
                    #O_turns.append(TURNS[i][j])
                #else:
                    #None
