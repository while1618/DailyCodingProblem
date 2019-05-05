# This problem was asked by Google.
#
# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
# Each False boolean represents a tile you can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required
# to reach the end coordinate from the start. If there is no possible path, then return null.
# You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
#
# For example, given the following board:
#
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end
# is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
#
# MyNote: Print all possible exits, for given example:
# ['RRRULUULL', 'RRUUULL', 'RURUULL', 'URRUULL', 'URDRRULUULL', 'URDRUUULL']

maze = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]
start = (3, 0)
end = (0, 0)
exits = []


def find_exits(row, column, current_path, direction):
    try:
        if row >= 0 and column >= 0 and not maze[row][column]:
            if (row, column) == end:
                current_path += direction
                exits.append(current_path)
            else:
                maze[row][column] = 'visited'
                current_path += direction
                find_exits(row, column + 1, current_path, "R")
                find_exits(row + 1, column, current_path, "D")
                find_exits(row, column - 1, current_path, "L")
                find_exits(row - 1, column, current_path, "U")
                maze[row][column] = False
    except IndexError:
        return


find_exits(start[0], start[1], '', '')
if not exits:
    print('You are doomed. No exit!')
else:
    print('Shortest path to end is ' + str(len(min(exits, key=len))) + ' steps long')
    print('All paths: ' + ', '.join(exits))
