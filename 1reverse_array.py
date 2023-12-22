def reverse_array(idx, numbers):
    if idx >= len(numbers)//2:
        print(' '.join(numbers))
        return
    numbers[idx], numbers[len(numbers)-1-idx] = numbers[len(numbers)-1-idx], numbers[idx]
    reverse_array(idx+1, numbers)
# nums = input().split()
nums = ['1', '2', '3', '4', '5', '6']
reverse_array(0, nums)


# def reverse_array(idx, numbers):
#     if idx >= len(numbers):
#         return
#     print(numbers[len(numbers)-1-idx], end=' ')
#     reverse_array(idx+1, numbers)
# # nums = input().split()
# nums = ['1', '2', '3', '4', '5', '6']
# reverse_array(0, nums)


# def reverse_array(numbers: list):  # SAME THING DIFFERENT WAY
#     if len(numbers) == 0:
#         return
#     print(numbers[-1], end=' ')
#     numbers.pop()
#     reverse_array(numbers)
# # nums = input().split(' ')
# nums = ['1', '2', '3', '4', '5', '6']
# reverse_array(nums)


# def reverse_array(idx, elements):
#     if idx >= len(elements) // 2:
#         return
#     other_side_idx = len(elements) - idx - 1
#     elements[idx], elements[other_side_idx] = elements[other_side_idx], elements[idx]
#     reverse_array(idx+1, elements)
#
#
#
# els = input().split()
# reverse_array(0, els)
# print(' '.join(els))


# def reverse_array(idx, elements, result):
#     if idx < 0:
#         return
#     result.append(elements[idx])
#     reverse_array(idx - 1, elements, result)
#
#
# elementi = input().split()
# reversed_elements = []
# reverse_array(len(elementi) - 1, elementi, reversed_elements)
# print(' '.join(reversed_elements))


# INPUT:
# 1 2 3 4 5 6