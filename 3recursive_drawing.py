def draw_symmetric_figure(n):
    if n == 0:
        # tova ti razpoluvqva broq iteracii
        # i ednovremenno
        return

    print(n * '*')
    draw_symmetric_figure(n - 1)
    print(n * '#')


n = int(input())
draw_symmetric_figure(n)


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

