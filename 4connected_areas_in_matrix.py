def find_all_areas(row, col, rows, cols, matrix):
    if row < 0 or col < 0 or row >= rows or col >= cols:
        return 0
    if matrix[row][col] == '*':  # if WALL
        return 0
    if matrix[row][col] == 'v':  # if VISITED
        return 0

    size_area = 1
    matrix[row][col] = 'v'

    size_area += find_all_areas(row+1, col, rows, cols, matrix)  # DOWN
    size_area += find_all_areas(row-1, col, rows, cols, matrix)  # UP
    size_area += find_all_areas(row, col+1, rows, cols, matrix)  # RIGHT
    size_area += find_all_areas(row, col-1, rows, cols, matrix)  # LEFT

    return size_area


rows = int(input())
cols = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
positions = []
for row in range(rows):  # walkthrough all rows and columns so that you enter their indexes
    for col in range(cols):  # in the function find_all_areas
        size = find_all_areas(row, col, rows, cols, matrix)
        if size != 0:
            positions.append((row, col, size))
print(f"Total areas found: {len(positions)}")

sorted_positions = sorted(positions, key=lambda x: -x[2])
for i in range(len(positions)):
    print(f"Area #{i+1} at ({sorted_positions[i][0]}, {sorted_positions[i][1]}), size: {sorted_positions[i][2]}")



# # INPUT 1:
# 4
# 9
# ---*---*-
# ---*---*-
# ---*---*-
# ----*-*--

# # INPUT 2:
# 5
# 10
# *--*---*--
# *--*---*--
# *--*****--
# *--*---*--
# *--*---*--