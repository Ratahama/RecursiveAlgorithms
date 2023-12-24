def draw_symmetric_figure(n: int):
    if n == 0:
        return
    print('*'*n)
    draw_symmetric_figure(n-1)
    print('#'*n)  # BACKTRACKING
draw_symmetric_figure(int(input()))


# # INPUT1:
# 2
# # OUTPUT1:
# **
# *
# #
# ##

# # INPUT2:
# 5
# # OUTPUT2:
# *****
# ****
# ***
# **
# *
# #
# ##
# ###
# ####
# #####


# # NOT WORKING IDEA:
# def draw_symmetric_figure(n: int):
#     if n == 0:
#         continue  # continue DOESN'T work here, shame
#     if n < 0:
#         print('#' * n)
#     print('*'*n)
#     draw_symmetric_figure(n-1)
# draw_symmetric_figure(int(input()))



# def draw_symmetric_figure(n):
#     if n == 0:
#         # tova ti razpoluvqva broq iteracii
#         # i ednovremenno
#         return
#
#     print(n * '*')
#     draw_symmetric_figure(n - 1)
#     print(n * '#')
# n = int(input())
# draw_symmetric_figure(n)


# # NOT WORKING
# def drawer(n):
#     if n > 0:
#         return (n * '*') + '\n' + drawer(n-1)
#     elif n < 0:
#         return ((-n) * '#') + '\n' + drawer(-(n+1))
#     else:
#         return ''
#
# print(drawer(2))

