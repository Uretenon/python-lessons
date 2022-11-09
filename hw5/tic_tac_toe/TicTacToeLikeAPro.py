import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle


class Player(NamedTuple):
    label: str  # присваивает игроку Х или 0
    color: str  # чтобы различать двух игроков по цвету


class Move(NamedTuple):  # координаты хода, выраженные туплем, содержащим значение координаты по абсциссе и ординате
    row: int
    col: int
    label: str = ""  # изначально значение каждой клетки пустое, а затем мы в него вставим х или о


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)


class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)  # итератор циклирующий между двумя игроками
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []  # выигрышная комбинация на поле после хода игрока
        self._current_moves = []  # сохраняет ходы игрока для проверки на комбинации
        self._has_winner = False  # проверка на выигрыш
        self._winning_combos = []  # лист всех выгрышных комбинаций
        self._setup_board()  # метод для хранения ходов и подсчета выигрышных комбинаций на основе ходов

    def _setup_board(self):
        self._current_moves = [  # создаем лист из листа координат каждой клетки поля (которые выражены классом Move)
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()  # присваиваем метод соответствующему атрибуту

    def _get_winning_combos(self):
        rows = [  # лист в листе, двигаемся по горизонтали, затем по вертикали, для координаты ячейки двигаемся по
            # ряду, move.col отвечает за начальное положение по столбцам, move.row по ряду. соответственно,
            # саблист rows содержит выигрышную комбинацию по каждому ряду, а внешний лист хранит все ряды
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]  # то бишь, если представлять для удобства, rows выглядит так: [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        # (на деле он конечно выглядит так: [((1,1),(1,2),(1,3)),...(3,9))]
        columns = [list(col) for col in
                   zip(*rows)]  # zip(*rows) пересоздает распакованный(*) rows, пересоздавая его так:
        # [(1,4,7), (2, 5, 8), (7, 8, 9)], а потом list(col) создает 3 отдельных листа выигрышных комбинаций по столбцам
        first_diagonal = [row[i] for i, row in enumerate(rows)]  # (1, 5, 9)
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]  # (7, 5, 3)
        return rows + columns + [first_diagonal, second_diagonal]

    def is_valid_move(self, move):  # сюда будет передаваться ход игрока через нажатие кнопки
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""  # если клетка пустая, то возвращает true
        no_winner = not self._has_winner  # проверка на победителя игры. Без этой строчки пустые кнопки будут
        # тыкабельны, даже если в игре уже определен победитель
        return no_winner and move_was_not_played

    def process_move(self, move):
        row, col = move.row, move.col
        self._current_moves[row][col] = move  # вносим ход игрока в ячейку соответствующей координаты из листа
        # координат всех ячеек, это также заменит лейбл этой клетки с пустого на х или о
        for combo in self._winning_combos:
            results = set(  # в каждой выигрышной комбинации необходимо узнать, состоит ли эта комбинация из только
                # нулей или крестиков, или же она смешанная. если она смешанная, то set-лист будет состоять из
                # нескольких элементов, а не одного
                self._current_moves[n][m].label for n, m in combo)
            is_win = (len(results) == 1) and ("" not in results)  # если в сет-листе 1 элемент(х или о), то будет
            # выигрыш
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def is_tied(self):  # для ничьи
        no_winner = not self._has_winner
        played_moves = (move.label for row in self._current_moves for move in row)  # я едва не сломался на этой строчке,
        # она создает генератор played_moves, который проверяет каждую клетку поля на значение лейбла (который будет
        # задан как not "") и возвращает True, если клетка не пустая. Первый for движется по столбцу, второй по ряду
        # (это очень странно выглядит, но на деле это просто внешний и внутренний for, который мы всегда пишем для
        # матрицы)
        return no_winner and all(played_moves)  # all() проверяет, весь ли генератор состоит из True. Если хотя бы
        # одна клетка пустая(то есть генератор выдал один False), то all() вернет False

    def has_winner(self):  # метод вернет true для соответствующего атрибута игры, если в игре есть победитель
        return self._has_winner

    def toggle_player(self):
        self.current_player = next(self._players)

    def reset_game(self):
        for row, row_content in enumerate(self._current_moves):  # двойным циклом проходимся по всем ячейкам и
            # обнуляем их, заменяя на стандартный пустой тупль
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []

class TicTacToeBoard(tk.Tk):
    def __init__(self, game):
        super().__init__()  # чтобы перенять метод инициалиции от родителя init применяем супер
        self.title = "Tic-Tac-Toe.v1"
        self._cells = {}  # создание словаря пустых клеток, из которых состоит поле
        self._game = game
        self._create_menu()
        self._create_board_display()
        self._create_board_grid()

    def _create_menu(self):
        menu_bar = tk.Menu(master=self)  # создаем меню сверху
        self.config(menu=menu_bar)  # делаем его частью нашего окна и добавляем в него различные функции
        file_menu = tk.Menu(master=menu_bar)
        file_menu.add_command(label="Play Again", command=self.reset_board)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def play(self, event):
        button_click = event.widget  # воспринимает текущее действие(event) как виджет (одна из кнопок на дисплее)
        row, col = self._cells[button_click]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(button_click)  # обновляет дисплей, заменяя пустое место на лейбл (х или о)
            # текущего хода с цветом игрока (метод описан ниже)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")  # (метод описан ниже)
            elif self._game.has_winner():
                self._highlight_cells()  # выделяет выигравшую комбинацию (метод описан ниже)
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
            else:
                self._game.toggle_player()  # переход хода к следующему игроку (метод описан выше)
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master = display_frame,
            text="Ready?",
                    font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(
            master=self)  # мастером фрейма (тело игры) будет объект типа фрейм библиотеки ткинтер
        grid_frame.pack()  # включение фрейма в пакет, чтобы он мог выполниться поочередно
        for row in range(self._game.board_size):  # заполнение фрейма клетками - кнопками
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=40, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (
                row, col)  # добавляем каждую кнопку в словарь клеток, чтобы с ними потом работать
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")  # делает то же самое что и .pack,
                # только для группы объектов в виде сетки

    def _update_button(self, button_click):
        button_click.config(text=self._game.current_player.label)
        button_click.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()


if __name__ == "__main__":
    main()
