def nested_loops(idx, sequence):
    if idx >= len(sequence):
        print(*sequence, sep=' ')
        return
    for i in range(1, len(sequence)+1):
        sequence[idx] = i
        nested_loops(idx+1, sequence)


n = int(input())
arr = [None] * n
nested_loops(0, arr)

