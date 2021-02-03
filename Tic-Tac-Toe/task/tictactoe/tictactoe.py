matrix = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
coord1 = None
coord2 = None
move = 0
x = 0
o = 0
p = 9


def print_matrix():
    ch = '---------'
    print(ch)
    print('|' + ' ' + matrix[0][0] + ' ' + matrix[0][1] + ' ' + matrix[0][2] + ' ' + '|')
    print('|' + ' ' + matrix[1][0] + ' ' + matrix[1][1] + ' ' + matrix[1][2] + ' ' + '|')
    print('|' + ' ' + matrix[2][0] + ' ' + matrix[2][1] + ' ' + matrix[2][2] + ' ' + '|')
    print(ch)


def enter_coord_x():
    coord_input = input('Enter the coordinates: ').split(' ')
    try:
        global coord1
        coord1 = int(coord_input[0])
        global coord2
        coord2 = int(coord_input[1])
    except ValueError:
        print('You should enter numbers!')
        enter_coord_x()

    if coord1 <= 0 or coord2 <= 0 or coord1 > 3 or coord2 > 3:
        print('Coordinates should be from 1 to 3!')
        enter_coord_x()

    if matrix[coord1 - 1][coord2 - 1] != '_':
        print('This cell is occupied! Choose another one!')
        enter_coord_x()

def field_valid(matrix):
    global x, o, p
    lst = sum(matrix, [])
    for i in range(len(lst)):
        if lst[i] == 'X':
            x += 1
        if lst[i] == 'O':
            o += 1
        # if lst[i] == '_':
        #     p += 1


def o_line(string):
    if (matrix[0][0] == matrix[0][1] == matrix[0][2] == 'O' or matrix[1][0] == matrix[1][1] == matrix[1][2] == 'O'
            or matrix[2][0] == matrix[2][1] == matrix[2][2] == 'O' or matrix[0][0] == matrix[1][0] == matrix[2][0] == 'O'
            or matrix[0][1] == matrix[1][1] == matrix[2][1] == 'O' or matrix[0][2] == matrix[1][2] == matrix[2][2] == 'O'
            or matrix[0][0] == matrix[1][1] == matrix[2][2] == 'O' or matrix[0][2] == matrix[1][1] == matrix[2][0] == 'O'):
        return True
    else:
        return False


def x_line(string):
    if (matrix[0][0] == matrix[0][1] == matrix[0][2] == 'X' or matrix[1][0] == matrix[1][1] == matrix[1][2] == 'X'
            or matrix[2][0] == matrix[2][1] == matrix[2][2] == 'X' or matrix[0][0] == matrix[1][0] == matrix[2][0] == 'X'
            or matrix[0][1] == matrix[1][1] == matrix[2][1] == 'X' or matrix[0][2] == matrix[1][2] == matrix[2][2] == 'X'
            or matrix[0][0] == matrix[1][1] == matrix[2][2] == 'X' or matrix[0][2] == matrix[1][1] == matrix[2][0] == 'X'):
        return True
    else:
        return False


def field_finish(matrix):
    # if abs(x - o) >= 2 or (x_line(matrix) == True and o_line(matrix) == True):
    #     print('Impossible')
    # elif x_line(matrix) == False and o_line(matrix) == False and p > 0:
    #     print('Game not finished')
    #     enter_coord_x()
    if x_line(matrix) == True:
        print_matrix()
        print('X wins')
        quit()
    elif o_line(matrix) == True:
        print_matrix()
        print('O wins')
        quit()
    elif x_line(matrix) == False and o_line(matrix) == False and p == 0:
        print_matrix()
        print('Draw')
        quit()


def choice_player():
    global move
    move += 1
    if move % 2 == 0:
        matrix[coord1 - 1][coord2 - 1] = 'O'
    else:
        matrix[coord1 - 1][coord2 - 1] = 'X'
    # field_valid(matrix)
    # field_finish(matrix)
    # start()

def start():
    global p, x, o
    print_matrix()
    enter_coord_x()
    choice_player()
    field_valid(matrix)
    p -= 1
    field_finish(matrix)
    start()

start()

