from turtle import *


# Общие функции
def DebugMsg(message, tab=0, isWarning=False):
    if isWarning:
        print('[W] '+ message)
        return

    if debug == 1:
        print(f'[D] ' + '|   '*tab + message)

def Panic(message):
    print(f'[E] {message}\n    Нажмите Enter чтобы выйти')
    input()
    quit()

def DrawAxis(size):
    if size==0: 
        return

    up()
    DebugMsg(f'Рисуем точки размером {size} в прямоугольнике размером {dr[0]} на {dr[1]}')

    for x in range(dr[0]*-s, dr[0]*s, s):
        for y in range(dr[1]*-s, dr[1]*s, s):
            goto(x,y)

            if x==o[0]*s and y==o[1]*s:
                dot(size*1.5, 'red')
                continue

            if x==o[0]*s or y==o[1]*s:
                dot(size*1.2, 'green')
                continue

            dot(size, 'blue')

# Парсеры
def CommandsSolver(Commands, Depth=0):
    '''
    Парсер команд, написан на if условиях для совместимости со старыми версиями Python 
    '''

    index = 0

    while index < len(Commands):
        Command = Commands[index]
        arg = Commands[index+1]

        DebugMsg(f'[Индекс {index}] {Command} {arg}', Depth)

        # Перемещение
        if Command in ('Вперёд', 'Вперед'):
            forward(int(arg)*s)
            index += 2
            continue

        if Command == 'Назад':
            backward(int(arg)*s)
            index += 2
            continue

        if Command == 'Направо':
            right(int(arg))
            index += 2
            continue

        if Command == 'Налево':
            left(int(arg))
            index += 2
            continue

        if Command == 'Сместиться':
            Coordinates = (Commands[index+2])[1:-1].split(',')
            DebugMsg(f'Координаты перемещения: {Coordinates}', Depth)
            goto(xcor() + int(Coordinates[0])*s, ycor() + int(Coordinates[1])*s)
            index += 3
            continue

        # След
        if Command == 'Поднять':
            up()
            index += 2
            continue

        if Command == 'Опустить':
            down()
            index += 2
            continue

        # Циклы
        if Command == 'Повтори':
            IteratedCommands = Commands[Commands.index('[')+1:]
            BracketCounter = 1

            # Поиск границ цикла
            for i in range(len(IteratedCommands)):
                IteratedCommand = IteratedCommands[i]

                if not IteratedCommand in '[]':
                    continue

                if IteratedCommand == '[':
                    BracketCounter += 1
                elif IteratedCommand == ']':
                    BracketCounter -= 1

                if BracketCounter == 0:
                    IteratedCommands = IteratedCommands[:i]
                    break
            else:
                Panic(f'Незакрытая скобка после ...[ {" ".join(IteratedCommands)}')

            DebugMsg(f'Инструкции цикла: {" ".join(IteratedCommands)}', Depth)

            for i in range(int(Commands[index+1])):
                DebugMsg(f'| Итерация {i}:', Depth)
                CommandsSolver(IteratedCommands, Depth+1)

            DebugMsg(f'| Конец цикла, индекс {index}', Depth)
            index += 4 + len(IteratedCommands)
            continue

        # TODO: Дописать удаление неправильных команд до следующей опознанной правильной команды
        DebugMsg(f'Неизвестная команда \'{Command}\' на индексе {index}', isWarning=True)
        break

def ParameterSolver(var, val):
    '''
    Парсер значений, тоже написан на if условиях для совместимости со старыми версиями Python 
    '''

    global s, o, r, d, dr, t, debug

    if var == 's':
        s = int(val)
        return

    if var == 'o':
        o = [int(p) for p in val.split(',')]
        return

    if var == 'r':
        r = int(val)
        return

    if var == 'd':
        d = int(val)
        return

    if var == 'dr':
        dr = [abs(int(p)) for p in val.split(',')]
        return

    if var == 't':
        t = int(val)
        return

    if var == 'debug':
        debug = int(val)
        return

    if var == 'reset':
        s, o, r, d, dr, t, debug = defaultParameters
        return

    DebugMsg(f'Неизвестный параметр \'{var}\', пропускаем', isWarning=True)

# Дефолтные значения
defaultParameters = [10, [0, 0], 0, 3, [10, 10], 10, 0]
Commands = []

s, o, r, d, dr, t, debug = defaultParameters

# Основной цикл
while True:
    reset()

    # Ввод
    UserInput = input('Параметры: ').replace(' ','').split(';')
    if UserInput != ['']:
        for el in UserInput:
            el = el.split('=')

            if len(el)==1:
                DebugMsg(f'Некорректный параметр \'{el[0]}\'', isWarning=True)
                continue

            ParameterSolver(el[0], el[1])

    UserInput = input('Команды: ')
    Commands = UserInput.replace('[','[ ').replace(']',' ]')
    Commands = Commands.replace('  ',' ') # это нужно для случаев, когда пробелы после скобок уже стоят
    Commands = Commands.split(' ')


    # Исполнитель
    if 1<=t<=10:
        speed(t)
    else:
        tracer(t,0) #альтернативный метод побыстрее

    left(r)
    up()
    goto(o[0]*s, o[1]*s)
    down()

    if Commands != ['']:
        CommandsSolver(Commands)

    DebugMsg('Конец программы')
    DrawAxis(d)

    # Перезапуск
    UserInput = input('Перезапустить? (Д/Н): ').lower()
    if not UserInput in ('д', 'да', 'y', '1'): 
        break

done()
