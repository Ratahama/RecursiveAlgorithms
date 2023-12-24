sequence = {}

def fibonacci(idx):
    if idx <= 1:
        return 1
    if idx in sequence.keys():
        return sequence[idx]
    result = fibonacci(idx-1) + fibonacci(idx-2)
    sequence[idx] = result
    return result



# u enter the position index in the fibonacci sequence
# and whats returned is the actual number in the fibonacci sequence on that position
# the fibonacci sequence goes like: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# idx = int(input())
print(fibonacci(8))