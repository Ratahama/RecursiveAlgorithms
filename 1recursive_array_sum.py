def array_sum(idx: int, nums: list, result: int):
    if idx >= len(nums):
        print(result)
        return
    result += nums[idx]
    array_sum(idx+1, nums, result)
sequence = [int(n) for n in input().split()]
array_sum(0, sequence, 0)


# # SECOND WAY:
# def array_sum(nums, idx):
#     if idx > len(nums) - 1:
#         return f"Index is too high, list hasn't got so many elements!"
#     if idx == len(nums)-1:
#         return nums[idx]
#     return nums[idx] + array_sum(nums, idx+1)
# nums = [int(num) for num in input().split(" ")]
# print(array_sum(nums, 0))


# INPUT:
# 1 2 3 4 5 6 7 8 9  >>>  45  ,pri idx=0
# 1 2 3 4	>>> 10            ,ako idx e 0
# -1 0 1    >>> 0             ,ako idx e 0


# An array is a data structure that stores values of the same type.
# In python, this is the main difference between arrays and lists.
# All values in an array must be of the same type,
# but they can be different types in a list.


# # WITHOUT RECURSION:
# def array_sum(nums, idx):
#     if idx > len(nums)-1:
#         return f"Index is too high, list hasn't got so many elements!"
#     elif idx == len(nums)-1:
#         return nums[idx]
#     total = 0
#     for i in range(idx, len(nums)):
#         total += nums[i]
#     return total
#
# nums = [int(num) for num in input().split(" ")]
# print(array_sum(nums, 0))
