# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


def getSumFromNumber(number):
    sum = 0
    while number:
        sum += number % 10
        number //= 10 
    return sum

def enterNumber() -> int:
    '''Возвращает целое число, введенное с терминала'''
    while True:
        a = input("Введите целое число: \n")
        try:
            a = int(a)
            return a
        except ValueError:
            print(f"{a} не яляется числом")

# 1ое решение
# ticket = input()
# print("yes" if getSumFromNumber(int(ticket[:3])) == getSumFromNumber(int(ticket[3:])) else "no")


# 2ое решение, если билет не шестизначный
ticket = enterNumber()
size = len(str(ticket))
second_part = ticket % 10**(size//2)
inc = 1 if size % 2 else 0
first_part = ticket // 10**(size//2 + inc)
if getSumFromNumber(first_part) == getSumFromNumber(second_part):
    print('yes')
else:
    print('no')    