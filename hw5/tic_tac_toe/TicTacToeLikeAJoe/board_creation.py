import constants


def createBoard(): # создаем доску размерХразмер
    board = [[constants.blank for x in range(constants.size)] for y in range(constants.size)]
    return board


def printBoard(board): # печатаем доску, чтобы было симпатично
    boundary = "------------"
    for i in range(constants.size):
        print(boundary + '-\n|', end='')
        for j in range(constants.size):
            print(" " + board[i][j] + " |", end='')
        print()
    print(boundary + '-')


def createBoardDict(board): # создаем словарь, в котором будем хранить значение каждой клетки, присваивая им номера
    # от 1 до 9. Так и играть легче, просто вписывая цифру от 1 до 9, и условия проверок будут без вложенных циклов
    k = 0
    board_dict = {}
    index = range(0, constants.size ** 2)
    for i in range(constants.size):
        for j in range(constants.size):
            board_dict[index[k] + 1] = board[i][j]
            k += 1
    return board_dict




