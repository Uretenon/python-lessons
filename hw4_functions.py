import random
from sympy import poly


def task(n, task_explanation):
    print(f'\nTask {n}\n')
    print(task_explanation, "\n")


def roundFromInput():
    d = int(input("Задайте точность d от 1 до 10: "))
    number = random.uniform(0, 10)
    print("Number: ", number)
    print(f"Number rounded to {d}: ", round(number, d))


def findPrimeFactors():
    n = int(input("Введите число: "))
    prime_list = []
    while n % 2 == 0:
        prime_list.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            prime_list.append(i)
            n = n // i
    if n > 2:
        prime_list.append(int(n))
    if len(prime_list) == 1:
        print("Число простое")
    else:
        print("Число раскладывается так: ", end='')
        print(*prime_list, sep=" * ")


def nonRepeatingElementsList():
    line = str(input("Введите строку: "))
    list_line = [(line[i:i + 1]) for i in range(0, len(line))]  # разрезаем строку на отдельные символы
    # создаем двойной цикл, внешний цикл двигается по разрезанной строке,
    # а внутренний проверяет каждый последующий элемент внешнего цикла на повторение и удаляет повторы
    for char in list_line:
        i = list_line.index(char) + 1
        while i < len(list_line):
            if char == list_line[i]:
                del list_line[i]
            else:
                i += 1
    print(list_line)


def polynomial(coeff, size):
    variable = 'x'
    coeff_list = []
    result = ''
    for i in range(0, coeff + 1):
        coeff_list.append(int(random.randrange(0, size)))
    for power, coeff in enumerate(coeff_list, start=-len(coeff_list) + 1):
        if coeff == 0:
            continue
        elif coeff == 1 and power != 0 and power != -1:
            result += '{}^{} {} '.format(variable, abs(power), random.choice(['-', '+']))
        elif coeff == 1 and power == -1:
            result += '{} {} '.format(variable, random.choice(['-', '+']))
        elif power == 0:
            result += '{} {} '.format(coeff, random.choice(['-', '+']))
        elif power == -1:
            result += '{}*{} {} '.format(coeff, variable, random.choice(['-', '+']))
        else:
            result += '{}*{}^{} {} '.format(coeff, variable, abs(power), random.choice(['-', '+']))
    polynom = "{}".format(result[:-3])
    print("Your polynomial:  ", polynom)
    return polynom


def polynomToFile(polynom, i):
    file = open(f"polynom{i}.txt", 'w')
    file.write(str(polynom))


def readPolynomFromFile(i):
    file = open(f"polynom{i}.txt", 'r')
    polynom = file.readline()
    return polynom

def polynomialSymPySum(pol1, pol2):
    summ = poly(pol1) + poly(pol2)
    result = str(summ.as_expr()).replace("**", "^")
    print("Polynomials sum: ", result)
    return result