def nested_loops(idx: int, nums: list):
    if idx >= len(nums):
        # print(' '.join([str(nu) for nu in nums]))  # needs to be a str to join it
        print(*nums, sep=' ')
        return
    for i in range(1, len(nums)+1):
        nums[idx] = i
        nested_loops(idx+1, nums)


n = int(input())
nested_loops(0, [0]*n)


# def nested_loops(idx, sequence):
#     if idx >= len(sequence):
#         print(*sequence, sep=' ')
#         return
#     for i in range(1, len(sequence)+1):
#         sequence[idx] = i
#         nested_loops(idx+1, sequence)
#
#
# n = int(input())
# arr = [None] * n  # VAJNO e da imash neshto v skobite dori i da e None
# nested_loops(0, arr)



# # INPUT1:
# 2
# # OUTPUT1:
# 1 1
# 1 2
# 2 1
# 2 2

# # INPUT2:
# 3
# # OUTPUT2:
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 1
# 1 2 2
# …
# 3 2 3
# 3 3 1
# 3 3 2
# 3 3 3