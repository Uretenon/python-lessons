import hw3_functions
import random
size = random.randrange(6, 10)
number = random.randrange(0, 55)
hw3_functions.task(1, 'Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции. Отсчет с нулевого элемента')
hw3_functions.oddSum(size)
hw3_functions.task(2, 'Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
hw3_functions.pairMultiplication(size)
hw3_functions.task(3, 'Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.')
hw3_functions.diffDecimal(size)
hw3_functions.task(4, 'Напишите программу, которая будет преобразовывать десятичное число в двоичное.')
print("Decimal number: ", number)
print("Result to binary: ", end="")
hw3_functions.decimalToBinary(number)
hw3_functions.task(5, 'Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.')
fib = []
for n in range (-size, size+1):
     fib.append(hw3_functions.negativeFib(n))
print(f' For {size} the negative Fibonacci sequence is:', end= " ")
print(fib, sep=", ")

