import random


f = open("chess_tree.txt")
dane = []
for i in f:
	dane.append(i)
chess_tree = " " + dane[3]


def RepresentsInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False


def next_move(tree):
	movex = ""
	opens = 0
	num = 0
	split = tree.split(" ")
	for i in split:
		if i == "(":
			opens += 1
		if opens == 0 and i != "":
			# print(i)
			movex += i
			movex = movex + " "
			num += 1
		if i == ")":
			opens += -1
		if opens < 0:
			break
		if num == 2:
			break	
	movex = movex.rstrip(" ")
	movex = movex.rstrip(")")
	movex = movex.rstrip(" ")
	return movex


def cut_tree(tree, move):
	# print(move)
	result = ""
	opens = 0
	ignore = 0
	if zamkniecie(tree)[0]:
		return tree[:zamkniecie(tree)[1]]
	else:
		tree2 = tree.replace(".", " ").split(" ")
		for i in tree2:
			if i == "(":
				opens += 1
			if opens == 1 and i == str(move):
				ignore = 1
			if i == ")":
				opens += -1
				if opens == 0 and ignore == 1:
					ignore = 0
			if not ignore:
				if RepresentsInt(i):
					result += i + "."
				else:
					result += i + " "
		# print(result)
		return result.rstrip(" ")
		
def zamkniecie(lista):
	opens = 0
	for i in range(len(lista)):
		if lista[i] == "(":
			opens += 1
		if lista[i] == ")":
			opens += -1
			if opens < 0:
				return True, i
	return False, i
	
	
def nawias(lista):
	opens = 0
	for i in range(len(lista)):
		if lista[i] == "(":
			opens += 1
		if lista[i] == ")":
			opens += -1
			if opens == 0:
				return lista[i:], i
	return False


def find_move(tree, move):
	if type(move) == list:
		[move] = move
	else:
		pass
	for i in range(len(tree)):
		if move == next_move(tree[i:]):
			return tree[i: ]
	return False


def find_all_moves_of_num_x(move, tree):
	num_move = ""
	pos_moves = []
	for i in range(len(tree) - 1):
		if tree[i + 1] == ".":
			if tree[i - 1] == " ":
				num_move = tree[i]
				if num_move == str(move):
					pos_moves.append(next_move(tree[i-1:]))
			else:
				num_move = tree[i-1] + tree[i]
				if num_move == str(move):
					pos_moves.append(next_move(tree[i-1:]))
	if pos_moves == []:
		return False
	return pos_moves


def train(tree):
	move = 1
	result = ""
	while True:
		if find_all_moves_of_num_x(move, tree):
			move_x = random.choices(find_all_moves_of_num_x(move, tree))
		else:
			break
		if find_move(tree, move_x) == False:
			break
		# print(find_move(tree, move_x))
		tree = cut_tree(find_move(tree, move_x), move)
		move += 1
		# print(move_x)
		move_x = move_x[0].split(".")
		move_x = move_x[::-1]
		result += move_x[0] + " "
	return result.rstrip(" ")


drzewo = []
def line_list(tree, move, line):
	if find_all_moves_of_num_x(move, tree):
		for i in find_all_moves_of_num_x(move, tree):
			line_list(cut_tree(find_move(tree, i), move), move + 1, line + i + " ")
	else:
		drzewo.append(line)


line_list(chess_tree, 1, "")






