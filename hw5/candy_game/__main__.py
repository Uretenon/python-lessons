import game_logic
mode = game_logic.gameStart()
if mode == 'pvp':
    game_logic.gamePVP()
else:
    game_logic.gamePVC()
