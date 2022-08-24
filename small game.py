from random import randrange

def display_board(board):
    print("+-------"*3,"+",sep="")
    for row in range(3):
        print("|       "*3,"|",sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="")

def enter_move(board):
    ok = False
    while not ok:
        move = input("Enter you move: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Bad move; Repeat move again: ")
            continue
        move = int(move) - 1
        row = move//3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['0','X']
        if not ok:
            print("FIeld already occupied; repeat again")
            continue
    board[row][col] = '0'


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['0','X']:
                free.append((row,col))
    return free

def victory_for(board, sign):
    if sign == 'X':
        who = 'me'
    elif sign== '0':
        who = 'you1'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            return who
        if board[0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            return who
        if board[rc][rc] != sign:
            cross1 = False
        if board[2 - rc][2 - rc] != sign:
            cross2 = False
    if cross1 or cross2:
        return who
    return None



def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # make an empty board
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn =  True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board,'0')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    human_turn = not human_turn
    free= make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("You won!")
elif victor == 'me':
    print("I won!")
else:
    print("Tie")