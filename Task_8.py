# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

def enterNumber(s) -> int:
    '''Возвращает целое число, введенное с терминала'''
    while True:
        a = input(f"{s} \n")
        try:
            a = int(a)
            return a
        except ValueError:
            print(f"{a} не яляется числом")

row = enterNumber("Введите количество продлольных линий шоколадки:")
column = enterNumber("Введите количество поперечных линий шоколадки:")
piecesToCut = enterNumber("Введите количество долек, которые нужно отломить:")
if (piecesToCut % row == 0 or piecesToCut % column == 0) and piecesToCut <= row * column:
    print("yes")
else:
    print("no")