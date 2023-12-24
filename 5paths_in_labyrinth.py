def find_all_paths(row, col, lab, direction, path):  # we always start from cell(0, 0)
    if row < 0 or col < 0 or row >= len(lab) or col >= len(lab[0]):
        return
    if lab[row][col] == '*':  # if this cell is a wall
        return
    if lab[row][col] == 'v':  # if its a visited cell
        return

    path.append(direction)
    if lab[row][col] == 'e':  # if on exit cell, finish this path
        print(''.join(path))
    else:  # if its not the exit, we make way
        lab[row][col] = 'v'  # marks cell as visited before moving on
        # in order to not return back to it in next recursive iterations
        # cuz you can get stuck moving back and forth on two cells forever

        find_all_paths(row-1, col, lab, 'U', path)
        find_all_paths(row+1, col, lab, 'D', path)
        find_all_paths(row, col-1, lab, 'L', path)
        find_all_paths(row, col+1, lab, 'R', path)

        lab[row][col] = '-'  # after going through the whole way we have to unmark the visited cells
        # ,as we backtrack our recursion, to make the cells available to other solutions

    path.pop()  # maha 'U', 'D', 'R', 'L' det si pisal
    # we take away the directions we've put in path in order to track a new pathway


rows = int(input())
columns = int(input())
lab = [list(input()) for i in range(rows)]
find_all_paths(0, 0, lab, '', [])  # we always start from cell(0, 0)


# # INPUT:
# 3
# 3
# ---
# -*-
# --e
# # OUTPUT:
# RRDD
# DDRR


# # INPUT:
# 3
# 5
# -**-e
# -----
# *****
# # OUTPUT:
# DRRRRU
# DRRRUR


