def path_counter(row: int, col: int, rows: int, cols: int):
    if row >= rows or col >= cols or row < 0 or col < 0:  # out-of-bounds
        return 0
    if row == rows-1 and col == cols-1:  # at exit
        return 1
    count = 0
    count += path_counter(row+1, col, rows, cols)  # DOWN
    count += path_counter(row, col+1, rows, cols)  # RIGHT
    return count


redove = int(input())
coloni = int(input())
# initial position is always 0, 0 topleft cell
# exit is always at downright-most cell
# count the amount of paths that can be trodden to the exit
print(path_counter(0, 0, redove, coloni))




# def path_counter(row, col, rows: int, cols: int):
#     if row >= rows or col >= cols:
#         return 0
#     if row == rows-1 and col == cols-1:
#         return 1
#
#     count = 0
#     count += path_counter(row, col+1, rows, cols)  # Right
#     count += path_counter(row+1, col, rows, cols)  # Down
#     return count
#
#
# redove = int(input())
# coloni = int(input())
# print(path_counter(0, 0, redove, coloni))


