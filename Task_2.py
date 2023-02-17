# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
def enterNumber() -> int:
    '''Возвращает целое число, введенное с терминала'''
    while true:
        a = input("Введите целое число")
        try:
            a = int(a)
            return a
        except ValueError:
            print(f"{a} не яляется числом")

n = enterNumber()
sum = 0
while n:
    sum += n % 10
    n //= 10
print(sum)