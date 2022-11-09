import move_logic
import board_creation
while True:
    board = board_creation.createBoard()
    board_dict = board_creation.createBoardDict(board)
    move_logic.gameStart(board, board_dict)
    yes = input("Хотите сыграть еще раз? Тогда напишите 1: ")
    if int(yes) != 1:
        break
