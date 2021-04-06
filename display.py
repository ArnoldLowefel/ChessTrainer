from tkinter import *

root = Tk()
root.title("Chess Board")
canvas = Canvas(root, width=600, height=600)

"""Squares"""
blacksquare = PhotoImage(file="Tiles/NPBS.png")
whitesquare = PhotoImage(file="Tiles/NPWS.png")
BBBS = PhotoImage(file="Tiles/BBBS.png")
BBWS = PhotoImage(file="Tiles/BBWS.png")
BKBS = PhotoImage(file="Tiles/BKBS.png")
BKWS = PhotoImage(file="Tiles/BKWS.png")
BNBS = PhotoImage(file="Tiles/BNBS.png")
BNWS = PhotoImage(file="Tiles/BNWS.png")
BPBS = PhotoImage(file="Tiles/BPBS.png")
BPWS = PhotoImage(file="Tiles/BPWS.png")
BQBS = PhotoImage(file="Tiles/BQBS.png")
BQWS = PhotoImage(file="Tiles/BQWS.png")
BRBS = PhotoImage(file="Tiles/BRBS.png")
BRWS = PhotoImage(file="Tiles/BRWS.png")
BSP = PhotoImage(file="Tiles/BSP.png")
WSP = PhotoImage(file="Tiles/WSP.png")
NPBS = PhotoImage(file="Tiles/NPBS.png")
NPWS = PhotoImage(file="Tiles/NPWS.png")
WBBS = PhotoImage(file="Tiles/WBBS.png")
WBWS = PhotoImage(file="Tiles/WBWS.png")
WKBS = PhotoImage(file="Tiles/WKBS.png")
WKWS = PhotoImage(file="Tiles/WKWS.png")
WNBS = PhotoImage(file="Tiles/WNBS.png")
WNWS = PhotoImage(file="Tiles/WNWS.png")
WPBS = PhotoImage(file="Tiles/WPBS.png")
WPWS = PhotoImage(file="Tiles/WPWS.png")
WQBS = PhotoImage(file="Tiles/WQBS.png")
WQWS = PhotoImage(file="Tiles/WQWS.png")
WRBS = PhotoImage(file="Tiles/WRBS.png")
WRWS = PhotoImage(file="Tiles/WRWS.png")


def draw_board(board, color, canva):
    """get board and color, board = table [len = 64] draw board on canvas"""
    if color == "w":
        sq = 0
    else:
        sq = 1
    for i in range(8):
        for j in range(8):
            _ = board[j*8+i]
            if sq == 0:
                if _ == "square":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=whitesquare)
                if _ == "K":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WKWS)
                if _ == "P":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WPWS)
                if _ == "Q":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WQWS)
                if _ == "N":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WNWS)
                if _ == "R":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WRWS)
                if _ == "B":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WBWS)
                if _ == "k":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BKWS)
                if _ == "p":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BPWS)
                if _ == "q":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BQWS)
                if _ == "n":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BNWS)
                if _ == "r":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BRWS)
                if _ == "b":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BBWS)
                sq += 1
            elif sq == 1:
                if _ == "square":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=blacksquare)
                if _ == "K":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WKBS)
                if _ == "P":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WPBS)
                if _ == "Q":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WQBS)
                if _ == "N":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WNBS)
                if _ == "R":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WRBS)
                if _ == "B":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=WBBS)
                if _ == "k":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BKBS)
                if _ == "p":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BPBS)
                if _ == "q":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BQBS)
                if _ == "n":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BNBS)
                if _ == "r":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BRBS)
                if _ == "b":
                    canva.create_image(i * 75, j * 75, anchor='nw', image=BBBS)
                sq -= 1
        if sq == 0:
            sq += 1
        else:
            sq -= 1


