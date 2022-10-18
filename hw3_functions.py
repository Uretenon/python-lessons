import random
import math


def task(n, task_explanation):
    print(f'\nTask {n}\n')
    print(task_explanation, "\n")
    input("Нажмите Enter, чтобы увидеть результат работы ")
    print()


def createNumList(size):
    list1 = [int(random.randrange(0, size ** 2)) for i in range(0, size)]
    print("List of random int numbers: ", list1)
    return list1


def createRealNumList(size):
    list1 = [float(random.uniform(0, size ** 2)) for i in range(0, size)]
    list1 = [round(num, 2) for num in list1]  # округлили для удобства
    print("List of random real numbers: ", list1)
    return list1


def oddSum(size):
    list1 = createNumList(size)
    sum = 0
    for i in range(1, size, 2):  # берем шаг 2 для только нечетных элементов
        sum += list1[i]
    print("Sum is:", sum)


def pairMultiplication(size):
    list1 = createNumList(size)
    mult = []
    n = math.floor(
        size / 2) + 1  # до центрального элемента с округлением вниз плюс еще один элемент, чтобы в нечетном варианте захватился центральный
    if n % 2 == 1:
        for i in range(0, n):
            mult.append(list1[i] * list1[size - i - 1])
    else:
        for i in range(0,
                       n - 1):  # т.к n идет до центрального, то минус 1, чтобы в четном варианте не брался лишний элемент
            mult.append(list1[i] * list1[size - i - 1])
    print("Result is: ", mult)


def diffDecimal(size):
    list1 = createRealNumList(size)
    max = float(0)  # берем максимум минимальным, проходимся по циклу, каждый раз находя большее значение - переприсваиваем макс
    min = 1  # берем минимум максимальным, проходимся по циклу, каждый раз находя меньшее значение - переприсваиваем мин
    for i in range(0, size):
        decimal = list1[i] - math.trunc(list1[i])  # чтобы получить дробную часть, из всего числа вычитаем целую часть
        if decimal < min:
            min = decimal
        if decimal > max:
            max = decimal
    diff = max - min
    print('Difference is: %.2f' % diff)


def decimalToBinary(number):  # простая рекурсия с оператором // для округления в нижнюю сторону
    if number >= 1:
        decimalToBinary(number // 2)
    print(number % 2, end='')

def negativeFib(n):
    if n > -1:
        if n == 0 or n == 1:
            return n
        else:
            return negativeFib(n - 1) + negativeFib(n - 2)
    if n <= -1:
        return ((-1) ** (abs(n) + 1)) * negativeFib(abs(n))  #тут долго соображал, потом дошло, что взяв модули, у нас не будут вылезать минусы не по формуле
