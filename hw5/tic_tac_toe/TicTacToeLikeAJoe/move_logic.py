import random
import win_or_not
import constants
from board_creation import printBoard


def playerTurn(name, symbol, board, board_dict,): # тут все просто, считываем ввод с клавы с кучей условий ошибок
    while True:
        move = input(f"Ход {name}: ")
        if move.strip() == '':
            print("Введите не пустое сообщение")
        else:
            try:
                move = int(move)
                assert 1 <= move <= 9
            except ValueError:
                print('Введите число')
            except AssertionError:
                print('Число должно быть от 1 до 9')
            else:
                if isValidMove(board_dict, move):
                    break
                else:
                    print('Ход можно делать только в пустую клетку. Попробуйте еще.')
    placeMove(board, board_dict, move, symbol) # тут используется метод хода, описанный ниже


def isValidMove(board_dict, move): # просто через словарик проверяем, занята ли клетка
    if board_dict[move] == constants.blank:
        return True
    return False


def placeMove(board, board_dict, move, symbol): # вписываем наш ход с клавы в доску и в словарь
    position = 0
    for i in board_dict:
        if i == move:
            board_dict[i] = symbol
            break
    for i in range(constants.size):
        for j in range(constants.size):
            position += 1
            if position == move:
                board[i][j] = symbol
                return


def gameStart(board, board_dict):
    print('Добро пожаловать в классическую игру "Крестики и нолики"! Надеюсь, правила вы знаете. Чтобы сделать ход, '
          'наберите число от 1 до 9 (расположение как на калькуляторе)')
    name1 = input("Игрок 1, введите имя: ")
    name2 = input("Игрок 2, введите имя: ")
    turn = random.choice([1, 2]) # рандомизируем кто ходит первый
    if turn == 2:
        name1, name2 = name2, name1
    printBoard(board)
    while True: # циклируем ходы игроков по очереди, каждый раз проверяя закончена ли игра
        playerTurn(name1, constants.x, board, board_dict,)
        if win_or_not.isGameFinished(board, board_dict, name1, name2):
            print("Игра окончена!")
            break
        printBoard(board)
        playerTurn(name2, constants.o, board, board_dict,)
        if win_or_not.isGameFinished(board, board_dict, name1, name2):
            print("Игра окончена!")
            break
        printBoard(board)
