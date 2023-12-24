def factorial_of(n):
    if n <= 1:
        return 1
    return n * factorial_of(n-1)
print(factorial_of(int(input())))


# # CLUMSIER WAY:
# def factorial_of(num: int, cache: int = 1):
#     if num <= 1:
#         print(cache)
#         return
#     cache *= num
#     num -= 1
#     factorial_of(num, cache)
# n = int(input("Enter factorial number: "))
# factorial_of(n)


# INPUT:
# 5  >>> 120
# 10 >>> 3628800