def path_counter(row, col, rows: int, cols: int):
    if row >= rows or col >= cols:
        return 0
    if row == rows-1 and col == cols-1:
        return 1

    count = 0
    count += path_counter(row, col+1, rows, cols)  # Right
    count += path_counter(row+1, col, rows, cols)  # Down
    return count


redove = int(input())
coloni = int(input())
print(path_counter(0, 0, redove, coloni))


