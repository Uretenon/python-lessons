import random


def playerTurn(name):
    while True:
        try:
            count = int(input(f"Ход фраерка по имени {name}. Забери до 28 конфет из кучи: "))
            assert 1 <= count <= 28
        except ValueError:
            print('Не хитри, фраерок! Конфет можно забрать только от 1 до 28')
        except AssertionError:
            print('Не хитри, фраерок! Конфет можно забрать только от 1 до 28')
        else:
            break
    return count
def computerTurn(candies):
    trigger = candies // 28
    if candies % 28 == 1 and trigger % 2 == 1:
        candies = 1
    elif candies % 28 == 1 and trigger % 2 == 0:
        candies = 28
    elif candies % 28 == 0 and trigger % 2 == 1:
        candies = 26
    elif candies % 28 == 0:
        candies = 27
    else:
        candies = candies - trigger * 28 - 1
    return candies




