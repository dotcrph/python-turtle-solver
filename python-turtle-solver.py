from turtle import *

def CommandsSolver(Commands):
    index=0
    while index < len(Commands):
        if debug==1: print('[D] Индекс:', index, ', Инструкция:', Commands[index])

        Command = Commands[index]
        if Command == 'Вперёд':
            forward(int(Commands[index+1])*s)
            index+=2
        elif Command == 'Назад':
            backward(int(Commands[index+1])*s)
            index+=2
        elif Command == 'Направо':
            right(int(Commands[index+1]))
            index+=2
        elif Command == 'Налево':
            left(int(Commands[index+1]))
            index+=2

        elif Command == 'Поднять':
            up()
            index+=2
        elif Command == 'Опустить':
            down()
            index+=2

        elif Command == 'Сместиться':
            Coordinates=Commands[index+2]
            Coordinates=(Coordinates[1:len(Coordinates)-1]).split(',')
            if debug==1: print('[D] Координаты перемещения:', Coordinates)
            goto(xcor()+int(Coordinates[0])*s,ycor()+int(Coordinates[1])*s)
            index+=3

        elif Command == 'Повтори':
            IteratedInstructions = Commands[Commands.index('[')+1:]

            # Поиск границ цикла
            IteratedInstructionsBuffer = IteratedInstructions.copy()
            while True: # Скорее всего, это всё можно сделать как то лучше, но мне как то лень над этим думать
                try:
                    BracketIndex=IteratedInstructionsBuffer.index('[')
                except:
                    break
                IteratedInstructionsBuffer[BracketIndex]=''
                IteratedInstructionsBuffer[IteratedInstructionsBuffer.index(']',BracketIndex)]=''
            BracketIndex=IteratedInstructionsBuffer.index(']')

            IteratedInstructions = IteratedInstructions[:BracketIndex]
            if debug==1: print('[D] Инструкции цикла:', IteratedInstructions)
            for i in range(int(Commands[index+1])):
                if debug==1: print('[D] Итерация номер', i,':')
                CommandsSolver(IteratedInstructions)
            if debug==1: print('[D] Конец цикла, индекс', index)
            index+=4+len(IteratedInstructions)
            
        else:
            print('ОШИБКА: неизвестная команда', Command, 'на индексе', index)
            break

def DrawAxis(size):
    if size==0: return
    up()
    if debug==1: print('[D] Рисуем точки размером', size, 'в прямоугольнике размером',dr[0],'на',dr[1])
    for x in range(-1*dr[0]*s,dr[0]*s,s):
        for y in range(-1*dr[1]*s,dr[1]*s,s):
            goto(x,y)
            if x==o[0]*s and y==o[1]*s:
                dot(size*1.5, 'red')
            elif x==o[0]*s or y==o[1]*s:
                dot(size*1.2, 'green')
            else: 
                dot(size, 'blue')


# Дефолтные значения
s=10; o=[0,0]; r=0; d=3; dr=[10,10]; t=10; debug=0; Commands=[]


while True:
    reset()

    # Ввод
    UserInput = (input('Параметры: ').replace(' ','')).split(';')

    for el in UserInput:
        el=el.split('=')

        el0=el[0]
        if el0 == 's':
            s = int(el[1])
        elif el0 == 'o':
            o = el[1].split(',')
            o = [int(p) for p in o]
        elif el0 == 'r':
            r = int(el[1])
        elif el0 == 'd':
            d = int(el[1])
        elif el0 == 'dr':
            dr = el[1].split(',')
            dr = [abs(int(p)) for p in dr]
        elif el0 == 't':
            t = int(el[1])
        elif el0 == 'debug':
            debug = int(el[1])
        elif el0 == 'reset':
            s=10; o=[0,0]; r=0; d=3; dr=[10,10]; t=10; debug=0
        else:
            if debug==1: print('[D] [W] Неизвестный параметр',el[0],'пропускаем')

    UserInput = input()
    if UserInput:
        Commands = UserInput.replace('[','[ ').replace(']',' ]')
        Commands = Commands.replace('  ',' ')    # это нужно для случаев, когда пробелы после скобок уже стоят
        Commands = Commands.split(' ')


    # Исполнитель
    if t<=10:
        speed(t)
    else:
        tracer(t,0) #альтернативный метод побыстрее

    left(r); up(); goto(o[0]*s,o[1]*s); down()

    if Commands: CommandsSolver(Commands)
    if debug==1: print('[D] Конец программы')

    DrawAxis(d)

    # Повтор
    UserInput = input('Перезапустить? (Д/Н): ')
    if not(UserInput=='Д' or UserInput=='д' or UserInput=='Y' or UserInput=='y' or UserInput=='1'): break

done()