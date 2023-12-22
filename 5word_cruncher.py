def word_cruncher(idx: int, el_count: dict, idx_el: dict, target: str, used_elements: list):
    if idx >= len(target):
        print(' '.join(used_elements))
        return
    if idx not in idx_el:
        return
    for el in idx_el[idx]:
        if el_count[el] == 0:  # SKIP UNUSED elements
            continue
        used_elements.append(el)
        el_count[el] -= 1

        word_cruncher(idx + len(el), el_count, idx_el, target, used_elements)

        used_elements.pop()
        el_count[el] += 1


elements = input().split(', ')
target = input()
# elements = ['Word', 'cruncher', 'cr', 'h', 'unch', 'c', 'r', 'un', 'ch', 'er', 'a']
# target = "Wordcruncher"

el_count = {}
idx_el = {}
for el in elements:
    if el in el_count:
        el_count[el] += 1
        continue
    if el in target:  # maha nesushtesvuvashti elementi kato 'a' za 'Wordcruncher'
        el_count[el] = 1

    try:
        index = 0
        while True:
            index = target.index(el, index)
            if index not in idx_el:
                idx_el[index] = []
            idx_el[index].append(el)
            index += len(el)
    except ValueError:
        pass
# for el in elements:
#     if el not in target:  # ELIMINATE/PASS useless elements
#         continue
#
#     if el not in el_count.keys():
#         el_count[el] = 0
#
#     for i in range(len(target)):  # COUNTER
#         if target[i:i+len(el)] == el:
#             el_count[el] += 1
#             if i not in idx_el:
#                 idx_el[i] = []
#             idx_el[i].append(el)
# print(el_count)
# # {'Word': 1, 'cruncher': 1, 'cr': 1, 'h': 1, 'unch': 1, 'c': 2, 'r': 3, 'un': 1, 'ch': 1, 'er': 1}  # WRONG
# # {'Word': 1, 'cruncher': 1, 'cr': 1, 'h': 1, 'unch': 1, 'c': 1, 'r': 1, 'un': 1, 'ch': 1, 'er': 1, 'a': 1}
# print(idx_el)
# # {0: ['Word'], 4: ['cruncher', 'cr', 'c'], 9: ['h'], 6: ['unch', 'un'], 8: ['c', 'ch'], 2: ['r'], 5: ['r'], 11: ['r'], 10: ['er']}
# # {0: ['Word'], 4: ['cruncher', 'cr', 'c'], 9: ['h'], 6: ['unch', 'un'], 8: ['c', 'ch'], 2: ['r'], 5: ['r'], 11: ['r'], 10: ['er']}
word_cruncher(0, el_count, idx_el, target, [])







# # INPUT1:
# text, me, so, do, m, ran
# somerandomtext
# # OUTPUT1:
# so me ran do m text

# # INPUT2:
# Word, cruncher, cr, h, unch, c, r, un, ch, er
# Wordcruncher
# # OUTPUT2:
# Word c r un ch er
# Word c r unch er
# Word cr un c h er
# Word cr un ch er
# Word cr unch er
# Word cruncher


# # INPUT3:
# tu, stu, p, i, d, pi, pid, s, pi
# stupid
# # OUTPUT3:
# s tu p i d
# s tu pi d
# s tu pid
# stu p i d
# stu pi d
# stu pid





# # COUNTER ama broi tva deto AZ iskam ,NE tova koeto batNasko iska
# for el in elements:
#     if el not in target:  # ELIMINATE/PASS useless elements
#         continue
#
#     if el not in el_count.keys():
#         el_count[el] = 0
#
#     for i in range(len(target)):  # COUNTER
#         if target[i:i+len(el)] == el:
#             el_count[el] += 1
#             if i not in idx_el:
#                 idx_el[i] = []
#             idx_el[i].append(el)