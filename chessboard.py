from tkinter import *
import time
import pgntofen
import import_tree
import display
import random


# fen = pgnConverter.getFullFen()

"""Global Variables"""
active_square = [True, True]
pgnConverter = pgntofen.PgnToFen()
move = 0

def read_fen(fen_data):
    """get FEN data return 8x8 matrix [len = 64] with P,K,Q..."""
    board = []
    y = 0
    for i in fen_data:
        if i == "/":
            y += 1
        if i == " ":
            return board
        if 57 > ord(i) > 48:
            for _ in range(int(i)):
                board.append("square")
        elif i != "/":
            board.append(i)


def board_to_fen(board, color="w", castling="KQkq", enpassant="-", halfmove="0", move="1"):
    """get board table [len = 64] and convert it to fen"""
    x = 0
    counter = 0
    result = ""
    for i in board:
        counter += 1
        if i == "square":
            x += 1
        else:
            if x > 0:
                result += str(x)
                x = 0
            result += str(i)
        if counter == 8:
            counter = 0
            if x > 0:
                result += str(x)
                x = 0
            result += "/"

    result = result + " " + color + " " + castling + " " + enpassant + " " + halfmove + " " + move
    return result


def move_piece(squarea, squareb, board):
    """take piece from square a and move it to square b"""
    squarea = [squarea[0]-1, squarea[1]-1]
    squareb = [squareb[0]-1, squareb[1]-1]
    piece = board[8*squarea[1]+squarea[0]]
    board[8 * squarea[1] + squarea[0]] = "square"
    board[8 * squareb[1] + squareb[0]] = piece
    return board_to_fen(board)


def click_on_board(x, y):
    if x < 600 and y < 600:
        return [x // 75 + 1, y // 75 + 1]


def activate_square(xy):
    global active_square
    active_square = [xy[0], xy[1]]
    # print(active_square)


def click(event):
	global active_square, fen, move
	if not active_square[0]:
        	activate_square(click_on_board(event.x, event.y))
	else:
		move += 1
		# fen = board_to_fen(move_piece(active_square, click_on_board(event.x, event.y), read_fen(fen)))
		display.draw_board(read_fen(fen[move]), "w", display.canvas)
		# active_square = [False, False]
	return event.x, event.y


fen = []

import_tree.line_list(import_tree.chess_tree)
tree = import_tree.drzewo
# print(tree)

x = random.choices(tree)
[x] = x
print(x)
for i in list(x.split(" ")):
	# print(i)
	if import_tree.RepresentsInt(i[0]):
		if import_tree.RepresentsInt(i[1]):
			i = i[3:]
		else:
			i = i[2:]
	pgnConverter.move(str(i))
	fen.append(pgnConverter.getFullFen())
	# print(fen)


display.draw_board(read_fen(fen[move]), "w", display.canvas)
	
display.canvas.bind('<Button-1>', click)
display.canvas.pack()

mainloop()
