import hw4_functions
import random

hw4_functions.task(1, 'Вычислить число c заданной точностью d')
hw4_functions.roundFromInput()
hw4_functions.task(2, 'Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N')
hw4_functions.findPrimeFactors()
hw4_functions.task(3, 'Задайте последовательность символов. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.')
hw4_functions.nonRepeatingElementsList()
hw4_functions.task(4, "Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.")
coeff = int(input("Введите k: "))
size= 100
polynom1 = hw4_functions.polynomial(coeff, size)
hw4_functions.polynomToFile(polynom1, 1)
hw4_functions.task(5, 'Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.')
input("Нажмите Enter, чтобы увидеть результат сложения и первичные многочлены (не забудьте проверить файлы)")
polynom2 = hw4_functions.polynomial(random.randrange(2,7), 7)
polynom3 = hw4_functions.polynomial(random.randrange(2,7), 7)
hw4_functions.polynomToFile(polynom2, 2)
hw4_functions.polynomToFile(polynom3, 3)
polynom02 = hw4_functions.readPolynomFromFile(2)
polynom03 = hw4_functions.readPolynomFromFile(3)
polynom_sum = hw4_functions.polynomialSymPySum(polynom02, polynom03)
hw4_functions.polynomToFile(polynom_sum, 'sum')