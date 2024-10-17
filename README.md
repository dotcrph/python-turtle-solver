# Python Turtle Solver
**Python Turtle Solver** - небольшой по размеру скрипт, предоставляющий более быстрый способ работы с черепашкой в Python. Он автоматизирует такие вещи, как масштаб рисунка, смещение рисунка по X и Y, начальный поворот черепашки, отрисовка координат и скорость рисования. Также поддерживает циклы.
## Синтаксис
### Параметры:
Список параметров:
1. `s` - масштаб рисунка _(стандартное значение - 10)_
2. `t` - скорость черепашки _(стандартное значение - 10)_
3. `r` - начальный поворот черепашки _(по часовой стрелке, стандартное значение - 0)_
4. `o` - смещение рисунка _(стандартное значение - 0, 0)_
5. `d` - размер точек координатной сетки _(стандартное значение - 1)_
6. `dr` - ширина и высота координатной сетки _(рисует координатную сетку в прямоугольнике с размерами в два раза больше заданных и серединой в начале координат, стандартное значение - 0,0)_
7. `debug` - вывод отладочных данных в консоль _(принимает значения 0 и 1 (выкл и вкл соответственно), стандартное значение - 0)_
8. `reset` - задать стандартные параметры _(не требует значения)_

Задавать все параметры не обязательно, незаданные параметры принимают свои стандартные значения. Помимо этого, значения параметров не отчищаются при перезапуске программы.
Также, параметры задаются через точку запятой, например `s=5; o=-2,2; d=3; dr=20,20; debug=1`
### Команды (инструкции):
Список команд:
1. `Вперёд x` - пойти вперёд на x точек
2. `Назад x` - пойти назад на x точек
3. `Направо x` - повернуться направо на x градусов
4. `Налево x` - повернуться налево на x градусов
5. `Поднять хвост` - перестать оставлять след
6. `Опустить хвост` - начать оставлять след
7. `Сместиться на (x,y)` - сместиться на x точек вперёд и y точек вправо
8. `Повтори x [...]` - повторить указанные в скобках команды x раз

Все команды задаются сплошным текстом, например `Повтори 5 [Повтори 10 [Вперёд 50 Направо 30] Сместиться на (20,-20)]`. На данный момент скрипт поддерживает только целочисленные значения x, так что при дробных значениях программа будет выдавать ошибку. При перезапуске программы также необязательно переписывать команды заново, достаточно просто нажать Enter и черепашка выполнит все те же самые команды.
