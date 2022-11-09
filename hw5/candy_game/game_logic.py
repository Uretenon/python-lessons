import random

import player_logic


def gameStart():
    print('Добро пожаловать в игру "Жадность фраера сгубила!"')
    print("Правила игры:\nНа столе лежит 2021 конфета. За один ход можно забрать не более чем 28 конфет.\nВы должны "
          "сделать так, чтобы последний ход был вашим. Тогда вы заберете все конфеты себе.")
    while True:
        choice = int(input("Введите '1', если хотите играть вдвоем. Введите '2', если хотите играть с компьютером: "))
        if choice == 1:
            return 'pvp'
        if choice == 2:
            return 'pvc'
        else:
            print("Введите 1 или 2.")


def gamePVP():
    print("Выбран режим фраер на фраера. Битва умов начинается!")
    candies = 2021
    count = 0
    name1 = str(input("Первый фраер, введи имя: "))
    name2 = str(input("Второй фраер, введи имя: "))
    turn = random.choice([1, 2])
    if turn == 2:
        name1, name2 = name2, name1
    print(name1, " ходит первый.")
    while candies > 28:
        candies -= player_logic.playerTurn(name1)
        print(f"Фраерок по имени {name1} оставил в куче {candies} конфет")
        count += 1
        if candies <= 28:
            break
        else:
            candies -= player_logic.playerTurn(name2)
            print(f"Фраерок по имени {name2} оставил в куче {candies} конфет")
            count += 1
    if count % 2 == 1:
        pvpWin(name2, name1, candies)
    else:
        pvpWin(name1, name2, candies)


def gamePVC():
    print("Решил побороться с полоумной железкой? Ну, давай, не подведи!")
    candies = 2021
    count1 = 0
    count2 = 0
    name1 = str(input("Введи имя, фраер: "))
    turn = random.choice([1, 2])
    if turn == 1:
        print(name1, " ходит первый.")
    else:
        print("Железка ходит первой.")
    while candies > 28:
        if turn == 1:
            candies -= player_logic.playerTurn(name1)
            print(f"Фраерок по имени {name1} оставил в куче {candies} конфет")
            count1 += 1
            if candies <= 28:
                break
            else:
                candies -= player_logic.computerTurn(candies)
                print(f"Железка оставила в куче {candies} конфет")
                count1 += 1
        else:
            candies -= player_logic.computerTurn(candies)
            print(f"Железка оставила в куче {candies} конфет")
            count2 += 1
            if candies <= 28:
                break
            else:
                candies -= player_logic.playerTurn(name1)
                print(f"Фраерок по имени {name1} оставил в куче {candies} конфет")
                count2 += 1
    if turn == 1:
        if count1 % 2 == 1:
            pvcWin(name1, 2)
        else:
            pvcWin(name1, 1)
    if turn == 2:
        if count2 % 2 == 1:
            pvcWin(name1, 1)
        else:
            pvcWin(name1, 2)

def pvpWin(name1, name2, candies):
        print(
            f"Поздравляю, {name1}. Сделай последний ход, забери оставшиеся конфеты у твоего оппонента и перестанешь быть фраерком")
        candies -= player_logic.playerTurn(name1)
        if candies <= 0:
            print(f'{name1}, ты теперь конфетный пахан, а не какой-то там фраер. Поздравляю!')
        else:
            print(f"Серьезно?! Ахахахах. Вот умора!\nДа ты, фраерок, либо глупый, либо добрый, что в целом одно и "
                  f"то же.\nНадеюсь, что {name2} не такой наивный, поэтому просто поздравляю его с победой.")


def pvcWin(name1, condition):
    if condition == 1:
        print(f"Поздравляю, {name1}, ты одержал победу над несколькими строчками кода! Небось гордишься собой, да?")
    if condition == 2:
        print("Ахахахах, м-даааа. Не стыдно проиграть трем строчкам кода?")
