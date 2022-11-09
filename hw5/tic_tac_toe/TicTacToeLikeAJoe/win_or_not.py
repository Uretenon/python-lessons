import constants
import board_creation

def winCon(board_dict, symbol):  # тут проверяем на победу
    indices = list(board_dict.values()) # создаем лист из индексов нашей доски
    count_blank = 0
    for i in range(len(indices)): # считаем есть ли у нас пустые места в доске
        if indices[i] == constants.blank:
            count_blank += 1
            break
    win = any(symbol == indices[a] == indices[b] == indices[c]
              for a, b, c in
              [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)])
    # простое перечисление всех 8 вариантов выигрыша. я сначала думал нафигачить циклами, но зачем? у меня на джаве
    # написано для n-размерных крестиков-ноликов, там да, пришлось повозиться. а тут простое если, проверка быстрее идет
    if win:
        return True
    elif count_blank == 0 and not win:
        return 'tie'
    else:
        return False


def isGameFinished(board, board_dict, name1, name2):
    if winCon(board_dict, constants.x) == 'tie' and winCon(board_dict, constants.o) == 'tie':
        board_creation.printBoard(board)
        print("Ничья!")
        return True
    elif winCon(board_dict, constants.o) != 'tie' and winCon(board_dict, constants.o): # тут очень странная ошибка
        # была, связанная с тем как return работает. если не писать != 'tie', то он почему-то return 'tie' считает за
        # true и в условие влезает, давая победу не тому игроку. я хз почему так
        board_creation.printBoard(board)
        print(name2, " выиграл!")
        return True
    elif winCon(board_dict, constants.x) != 'tie' and winCon(board_dict, constants.x):
        board_creation.printBoard(board)
        print(name1, " выиграл!")
        return True
    else:
        return False

