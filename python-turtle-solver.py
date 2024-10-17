from turtle import *

def CommandsSolver(Commands):
    index=0
    while index < len(Commands):
        if debug==1: print('[D] Индекс:', index, ', Инструкция:', Commands[index])
        match Commands[index]:
            case 'Вперёд':
                forward(int(Commands[index+1])*s)
                index+=2
            case 'Назад':
                backward(int(Commands[index+1])*s)
                index+=2
            case 'Направо':
                right(int(Commands[index+1]))
                index+=2
            case 'Налево':
                left(int(Commands[index+1]))
                index+=2

            case 'Поднять':
                up()
                index+=2
            case 'Опустить':
                down()
                index+=2

            case 'Сместиться':
                Coordinates=Commands[index+2]
                Coordinates=(Coordinates[1:len(Coordinates)-1]).split(',')
                if debug==1: print('[D] Координаты перемещения:', Coordinates)
                goto(xcor()+int(Coordinates[0])*s,ycor()+int(Coordinates[1])*s)
                index+=3

            case 'Повтори':
                IteratedInstructions = Commands[Commands.index('[')+1:len(Commands)-(Commands[::-1]).index(']')-1]
                if debug==1: print('[D] Инструкции цикла:', IteratedInstructions)
                for i in range(int(Commands[index+1])):
                    if debug==1: print('[D] Итерация номер', i,':')
                    CommandsSolver(IteratedInstructions)
                if debug==1: print('[D] Конец цикла, индекс', index)
                index+=4+len(IteratedInstructions)
            
            case _:
                print('ОШИБКА: неизвестная команда', Commands[index], 'на индексе', index)
                break

def DrawAxis(size):
    if size==0: return
    up()
    if debug==1: print('[D] Рисуем точки размером', size, 'в прямоугольнике размером',dr[0],'на',dr[1])
    for x in range(-1*dr[0]*s,dr[0]*s,s):
        for y in range(-1*dr[1]*s,dr[1]*s,s):
            goto(x,y)
            dot(size, 'blue')


# Дефолтные значения
s=10; o=[0,0]; r=0; d=1; dr=[0,0]; t=10; debug=0


while True:
    reset()

    # Ввод
    UserInput = (input('Параметры: ').replace(' ','')).split(';')

    for el in UserInput:
        el=el.split('=')
        match el[0]:
            case 's':
                s = int(el[1])
            case 'o':
                o = el[1].split(',')
                o = [int(p) for p in o]
            case 'r':
                r = int(el[1])
            case 'd':
                d = int(el[1])
            case 'dr':
                dr = el[1].split(',')
                dr = [abs(int(p)) for p in dr]
            case 't':
                t = int(el[1])
            case 'debug':
                debug = int(el[1])
            case _:
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

    right(r); up(); goto(o[0],o[1]); down()

    CommandsSolver(Commands)
    if debug==1: print('[D] Конец программы')

    DrawAxis(d)

    # Повтор
    UserInput = input('Перезапустить? (Д/Н): ')
    if not(UserInput=='Д' or UserInput=='д' or UserInput=='Y' or UserInput=='y' or UserInput=='1'): break
    
done()