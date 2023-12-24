def factorial_of(n):
    if n == 0:
        return 1
    return n * factorial_of(n-1)


print(factorial_of(int(input())))

# INPUT:
# 5  >>> 120
# 10 >>> 3628800