import math
import random
print('1. Напишите программу, которая принимает на вход строку и показывает сумму всех ее цифр.\n')

number = input("type in a string: ")
sum = 0
for digit in number:
    if digit.isdigit():     # проверили, что символ это цифра и приплюсовали к сумме
        temp = int(digit)
        sum += temp
print('the sum of numbers is: ', sum)

print('\n2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.\n')

number = int(input('type in a number: '))
product2 = 1
for i in range(1, number):
    product2 *= i
    print(product2, end=', ')
print(product2 * number)
print ('bonus for Task 2: ') # в какой-то момент до меня дошло, что это факториал
for i in range(1, number+1):
  print(math.factorial(i), end = " ")

print('\n3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.\n')

n = int(input('input n: '))
sum4 = 0
print("{", end='')
for i in range(1, n):
    element = (1+1/i)**i
    sum4 += element
    el_format = '{0:.3g}'.format(element)
    print(f'{i}:{el_format}', end=", ")
element = (1+1/n)**n
sum4 += element
el_format = '{0:.3g}'.format(element)
print(f'{i}:{el_format}', end="}")
print("\nSum: %.2f" % sum4)

print("\n4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов "
      "на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.\n")

n = 10
input('type in anything to proceed ')
list1 = [int(random.randrange(-n, n)) for i in range(0, n)] # реализовали список, заполнив его случайными числами из
# промежутка [-n, n]
print('initial list: ', list1)

file = open("numbers.txt", 'w')
for i in range (0, int(n / 2)):
    file.write(str(random.randrange(1, n)) + '\n')  # нарандомили 5 (так выбрал, можно сколько угодно писать) позиций
file.close()
file = open("numbers.txt", 'r')
indices = [line.strip() for line in file.readlines()] # прочитали файл и внесли в лист все числа в одну строку
indices = [int(num) for num in indices] # чтобы с ним работать, преобразовали в тип int из типа str
print('List of indexes for multiplication: ', indices)
product4 = 1
for index in indices:
    product4 *= list1[index-1] # считаем произведение
print("The result:", product4)
random.shuffle(indices) # по фану(заданию) перемешали список
print("Mixing the index list for some reason:", indices)

print("\n5. Даны два массива, нужно вернуть их пересечение\n")


list1 = [1, 2, 3, 2, 0]
print(list1)
list2 = [5, 1, 2, 7, 3, 2]
print(list2)
input('type in anything to see the result ')
list3 = []
for i in range (0, len(list1)):
    for j in range (0, len(list2)):
        if list1[i] == list2[j]:
            list3.append(list1[i])
            list2.remove(list2[j])
            break
print("Intersection: ", list3)

