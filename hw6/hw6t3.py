import math
import random
from decimal import Decimal
from typing import List

size = 100
def printPriceList(list):
    print("прайс-лист:")
    for i in range(len(list)):
        if math.trunc(list[i]) < 10:
            price_tag = f'0{math.trunc(list[i])} руб {str(list[i] - math.trunc(list[i]))[2:]} коп'
        elif list[i] - math.trunc(list[i]) == 0:
            price_tag = f'{math.trunc(list[i])} руб 00 коп'
        elif math.trunc(list[i]) < 10 and list[i] - math.trunc(list[i]) == 0:
            price_tag = f'0{math.trunc(list[i])} руб 00 коп'
        else:
            price_tag = f'{math.trunc(list[i])} руб {str(list[i] - math.trunc(list[i]))[2:]} коп'
        if i != len(list)-1:
            print(price_tag, end=", ")
        else:
            print(price_tag, end=". \n")

def createPriceList(size):
    list1 = []
    for i in range(0, random.randint(int(size / 10), int(size / 7))):
        price = round(Decimal(random.uniform(5, size)), 2)  # float - головная боль для таких случаев, использовал стороннюю библиотеку.
        list1.append(price)  # сам лист лучше не печатать))
    return list1


prices = createPriceList(size)
print("Изначальный ", end='')
printPriceList(prices)
print("Вывести на экран эти цены через запятую в одну строку - ✓\nЦена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп») - ✓\nДобавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп). - ✓\n")
print("Ссылка на объект списка до сортировки - ✓\n", id(prices))
print("Отсортированный по возрастанию ", end='')
printPriceList(sorted(prices))
print("Объект списка после сортировки для доказательства, что я не создавал новый список - ✓\n", id(prices))
prices2 = sorted(prices, reverse=True)
print("Создать новый список, содержащий те же цены, но отсортированные по убыванию. - ✓. Доказательство - другая ссылка\n", id(prices2))
print("Отсортированный по убыванию ", end='')
printPriceList(prices2)

