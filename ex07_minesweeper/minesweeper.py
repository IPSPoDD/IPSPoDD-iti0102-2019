"""Minesweeper has to swipe the mines."""
import copy


def create_minefield(height: int, width: int) -> list:
    """
    Create and return minefield.

    Minefield must be height high and width wide. Each position must contain single dot (`.`).
    :param height: int
    :param width: int
    :return: list
    """
    matrix = [["." for x in range(width)] for y in range(height)]
    return matrix


def add_mines(minefield: list, mines: list) -> list:
    """
    Add mines to a minefield and return minefield.

    This function cannot modify the original minefield list.
    Minefield must be length long and width wide. Each non-mine position must contain single dot.
    If a position is empty ("."), then a small mine is added ("x").
    If a position contains small mine ("x"), a large mine is added ("X").
    Mines are in a list.
    Mine is a list. Each mine has 4 integer parameters in the format [N, S, E, W].
        - N is the distance between area of mines and top of the minefield.
        - S ... area of mines and bottom of the minefield.
        - E ... area of mines and right of the minefield.
        - W ... area of mines and left of the minefield.
    :param minefield: list
    :param mines: list
    :return: list
    """
    h = len(minefield)
    w = len(minefield[0])
    minnoje_pole = copy.deepcopy(minefield)
    for l_mines in mines:
        for i in range(h):
            for j in range(w):
                if (i >= l_mines[0]) and (i < h - l_mines[1]) and (j >= l_mines[3]) and (j < w - l_mines[2]) and (
                        minnoje_pole != 'X'):
                    if (minnoje_pole[i][j] == 'x'):
                        minnoje_pole[i][j] = 'X'
                    else:
                        minnoje_pole[i][j] = 'x'
    return minnoje_pole


def get_minefield_string(minefield: list) -> str:
    """
    Return minefield's string representation.

    .....
    .....
    x....
    Xx...

    :param minefield:
    :return:
    """
    min = "\n".join(["".join(i) for i in minefield])
    return min


def calculate_mine_count(minefield: list) -> list:
    """
    For each cell in minefield, calculate how many mines are nearby.

    This function cannot modify the original list.
    So, the result should be a new list (or copy of original).

    ....
    ..x.
    X.X.
    x..X

    =>

    0111
    13x2
    X4X3
    x32X

    :param minefield:
    :return:
    """
    h = len(minefield)
    w = len(minefield[0])
    minnoje_pole = copy.deepcopy(minefield)
    for k in range(h):
        for m in range(w):
            if (minnoje_pole[k][m] != 'X') and (minnoje_pole[k][m] != 'x'):
                n = 0
                for i in range(k - 1, k + 2):
                    for j in range(m - 1, m + 2):

                        if ((i >= 0) and (j >= 0) and (i < h) and (j < w)):
                            if (minnoje_pole[i][j] == 'x') or (minnoje_pole[i][j] == 'X'):
                                n += 1
                minnoje_pole[k][m] = str(n)
    return minnoje_pole


def find_sharp(minnoje_pole):  # or minefield
    """
    Find # in the field.

    Return coordinate or minefield without # ?

    :param minnoje_pole:
    :return:
    """
    for i in range(len(minnoje_pole)):
        for j in range(len(minnoje_pole[0])):
            if minnoje_pole[i][j] == "#":
                minnoje_pole[i][j] = "."
                return [i, j]
    return [0, 0]


def mines_count(minefield, i, j):
    """
    Count mines around the area.

    :param minefield:
    :param i:
    :param j:
    :return:
    """
    v = calculate_mine_count(minefield)
    return v[i][j]


def move(minnoje_pole, lives, coordinates, direction):
    """
    Move.

    :param minnoje_pole:
    :param lives:
    :param coordinates:
    :param direction:
    :return:
    """
    i = coordinates[0]
    j = coordinates[1]

    k = i + direction[0]
    m = j + direction[1]

    if (k >= 0) and (m >= 0) and (k < len(minnoje_pole)) and (
            m < len(minnoje_pole[0])):

        if (minnoje_pole[k][m] == "."):
            minnoje_pole[k][m] = "#"
            return lives

        if (minnoje_pole[k][m] == "x"):
            minnoje_pole[i][j] = "#"
            minnoje_pole[k][m] = "."
            if int(mines_count(minnoje_pole, i, j)) >= 5:
                lives -= 1
            return lives

        if (minnoje_pole[k][m] == "X"):
            if lives > 0:
                minnoje_pole[k][m] = "#"
                lives -= 1
                return lives
            else:
                return lives
    else:
        minnoje_pole[i][j] = "#"
        return lives

    return lives


def walk(minefield, moves, lives) -> list:
    """
    Make moves on the minefield.

    This function cannot modify the original minefield list.
    Starting position is marked by #.
    There is always exactly one # on the field.
    The position you start is an empty cell (".").

    Moves is a list of move "orders":
    N - up,
    S - down,
    E - right,
    W - left.

    Example: "NWWES"

    If the position you have to move contains "x" (small mine),
    then the mine is cleared (position becomes "."),
    but you cannot move there.
    In case of clearing a small mine, ff the position where the minesweeper is, has 5 or more mines nearby
    (see the previous function), minesweeper also loses a life.
    If it has 0 lives left, then clearing is not done and moving stops.

    Example:
    #x
    ..
    moves: ESS

    =>

    1st step ("E"):
    #.
    ..

    2nd step ("S"):
    ..
    #.

    3rd step ("S"):
    ..
    #.

    Example #2
    XXX
    x.x
    .#X
    moves: NWES, lives = 1

    1) "N"
    XXX
    x#x
    ..X

    2) "W". the small mine is cleared, but with the cost of one life :'(
    XXX
    .#x
    ..X
    lives = 0

    3) "E"
    XXX
    .#x
    ..X
    As clearing the mine on the right, he would lose a life (because minesweeper has 5 or more mines nearby).
    But as he has no lives left, he stops there. No more moves will be carried out.

    If the position you have to move contains "X" (huge mine),
    then you move there and lose a life.

    #X
    ..
    moves: ESS

    1) (lives = lives - 1)
    .#
    ..
    2)
    ..
    .#
    3)
    ..
    .#

    If you have to move into a position with a huge mine "X"
    but you don't have any more lives, then you finish your moves.

    lives: 2

    #XXXX
    .....
    moves: EEES

    1) lives = 1
    .#XXX
    .....
    2) lives = 0
    ..#XX
    .....
    3) stop, because you would die
    final result:
    ..#XX
    .....

    :param minefield:
    :param moves:
    :param lives:
    :return:
    """
    # i = 1
    minnoje_pole = copy.deepcopy(minefield)
    for destination in moves:
        if lives > 0:
            coordinates = find_sharp(minnoje_pole)
            if destination == "N":
                lives = move(minnoje_pole, lives, coordinates, [-1, 0])
            if destination == "S":
                lives = move(minnoje_pole, lives, coordinates, [1, 0])
            if destination == "E":
                lives = move(minnoje_pole, lives, coordinates, [0, 1])
            if destination == "W":
                lives = move(minnoje_pole, lives, coordinates, [0, -1])
    if lives == 0:
        return minnoje_pole
    return minnoje_pole


if __name__ == '__main__':
    minefield_a = create_minefield(4, 3)
    print(minefield_a)  # ->
    """
    [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    """

    minefield_a = add_mines(minefield_a, [[0, 3, 2, 0], [2, 1, 0, 1]])
    print(minefield_a)  # ->
    """
    [
        ['x', '.', '.'],
        ['.', '.', '.'],
        ['.', 'x', 'x'],
        ['.', '.', '.']
    ]
    """

    print(get_minefield_string(minefield_a))
    minefield_ac = calculate_mine_count(minefield_a)
    print(get_minefield_string(minefield_ac))

    minefield_b = create_minefield(8, 7)
    minefield_b = add_mines(minefield_b, [[2, 1, 3, 2], [0, 5, 3, 0]])

    print(minefield_b)  # ->
    """
    [
        ['x', 'x', 'x', 'x', '.', '.', '.'],
        ['x', 'x', 'x', 'x', '.', '.', '.'],
        ['x', 'x', 'X', 'X', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', 'x', 'x', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']
    ]
    """

    minefield_c = create_minefield(5, 5)
    minefield_c = add_mines(minefield_c, [[0, 0, 2, 2]])
    print(minefield_c)  # ->
    """
    [
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.'],
        ['.', '.', 'x', '.', '.']
    ]
    """

    mf = [['.', '.', '.', '.'], ['.', '.', 'x', '.'], ['X', '.', 'X', '.'], ['x', '.', '.', 'X']]
    print(calculate_mine_count(mf))

    """
    [
        ['0', '1', '1', '1'],
        ['1', '3', 'x', '2'],
        ['X', '4', 'X', '3'],
        ['x', '3', '2', 'X']
    ]
    """

    mf = copy.deepcopy(minefield_c)
    mf[0][0] = '#'
    print(get_minefield_string(walk(mf, "WEESE", 2)))
    """
    .....
    .#...
    ..x..
    ..x..
    ..x..
    """

    mf = create_minefield(3, 5)
    mf = add_mines(mf, [[0, 0, 1, 2]])
    mf = add_mines(mf, [[0, 1, 1, 1]])
    print(get_minefield_string(mf))
    """
    .xXX.
    .xXX.
    ..xx.
    """
    mf[0][4] = "#"
    mf = walk(mf, "WSSWN", 2)
    print(get_minefield_string(mf))
    """
    .xX..
    .xX#.
    ..x..
    """
    # minesweeper would die if stepping into the mine, therefore he stops
