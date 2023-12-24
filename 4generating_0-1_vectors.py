def gen01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        gen01(idx+1, vector)


i = int(input())
v = [1] * i  # whether its [0] or [1] doesn't matter ,cuz it gets reset to [0,0,0,0]
gen01(0, v)


# FOR INPUT: i=3 ,must return:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111

# # FOR INPUT: 1=5  , must print:
# 00000
# 00001
# 00010
# 00011
# 00100
# 00101
# 00110
# 00111
# 01000
# 01001
# 01010
# 01011
# 01100
# 01101
# 01110
# 01111
# 10000
# 10001
# 10010
# 10011
# 10100
# 10101
# 10110
# 10111
# 11000
# 11001
# 11010
# 11011
# 11100
# 11101
# 11110
# 11111




# print(*vector, sep='')
# # vectors are represented as lists or arrays,
# # so we unpack the list separating each element with nothing
# # so it prints as a single string

