data = [list(map(int, r.split())) for r in open('26_12933.txt').readlines()]
data = [
    (30, 50),
    (100, 155),
    (150, 170),
    (10, 160),
    (120, 55)
]
data_shlif = [data[idx][0] for idx in range(len(data))]
data_color = [data[idx][1] for idx in range(len(data))]

res_color = []
res_shlif = []


while data_color or data_shlif:
    min_color = min(data_color)
    idx_of_color = data_color.index(min_color)

    min_slif = min(data_shlif)
    idx_of_slif = data_shlif.index(min_slif)

    if min_slif > min_color:
        res_color.append(idx_of_color)
        data_color.pop(idx_of_color)
        data_shlif.pop(idx_of_color)

    else:
        res_shlif.append(idx_of_slif)
        data_color.pop(idx_of_slif)
        data_shlif.pop(idx_of_slif)

res = res_shlif + res_color[::-1]
print(res)
# print(len([948, 924, 317, 536, 287, 13, 92, 74, 261, 560, 390, 186, 832, 40, 764, 658, 296, 15, 245, 534, 771, 598, 367, 708, 677, 279, 251, 229, 391, 183, 219, 373, 634, 906, 465, 612, 818, 412, 617, 893, 919, 628, 683, 160, 690, 503, 451, 67, 682, 645, 688, 663, 437, 351, 531, 31, 719, 397, 813, 695, 421, 249, 333, 128, 13, 190, 226, 336, 606, 79, 464, 46, 753, 2, 525, 98, 289, 543, 642, 114, 465, 113, 765, 437, 257, 193, 715, 170, 566, 512, 339, 413, 736, 696, 748, 127, 605, 672, 286, 573, 571, 614, 452, 359, 599, 473, 467, 130, 655, 289, 659, 465, 325, 707, 26, 657, 276, 689, 419, 587, 116, 65, 742, 97, 279, 431, 267, 443, 301, 352, 213, 160, 42, 181, 51, 65, 641, 327, 656, 709, 220, 536, 678, 435, 278, 292, 617, 318, 708, 24, 453, 13, 267, 162, 602, 619, 32, 520, 38, 263, 311, 330, 448, 479, 472, 210, 451, 147, 140, 580, 242, 601, 198, 442, 342, 568, 295, 238, 521, 432, 542, 181, 87, 501, 380, 534, 234, 378, 614, 529, 69, 70, 274, 376, 227, 57, 522, 230, 199, 508, 452, 391, 524, 74, 59, 105, 65, 128, 576, 11, 438, 309, 148, 258, 116, 45, 155, 213, 484, 52, 417, 45, 168, 202, 411, 62, 362, 1, 106, 269, 177, 344, 540, 413, 31, 51, 44, 416, 122, 362, 140, 21, 441, 66, 246, 156, 366, 334, 263, 471, 400, 434, 280, 195, 372, 39, 161, 112, 44, 346, 35, 197, 28, 452, 331, 184, 267, 48, 458, 59, 372, 38, 77, 307, 344, 126, 244, 131, 373, 243, 300, 30, 438, 257, 148, 278, 89, 386, 55, 62, 280, 264, 296, 239, 170, 127, 408, 242, 157, 82, 181, 178, 291, 391, 117, 265, 25, 241, 251, 57, 182, 242, 158, 8, 202, 9, 7, 157, 257, 87, 93, 62, 90, 299, 346, 341, 330, 248, 289, 140, 159, 315, 308, 96, 177, 73, 274, 317, 256, 52, 106, 30, 44, 35, 153, 290, 135, 279, 61, 24, 123, 65, 123, 280, 112, 83, 43, 97, 111, 110, 182, 6, 107, 163, 214, 174, 20, 22, 98, 131, 135, 4, 129, 71, 91, 104, 183, 181, 18, 75, 207, 203, 0, 59, 90, 44, 44, 16, 111, 13, 60, 41, 19, 134, 193, 91, 183, 107, 132, 176, 75, 46, 2, 129, 147, 20, 166, 2, 87, 47, 88, 42, 68, 56, 125, 41, 63, 38, 35, 76, 131, 42, 141, 113, 12, 110, 131, 77, 85, 11, 52, 55, 94, 20, 6, 40, 29, 22, 74, 2, 1, 30, 51, 30, 52, 73, 45, 77, 11, 34, 88, 9, 57, 76, 43, 50, 66, 47, 26, 1, 23, 54, 24, 24, 11, 25, 25, 31, 23, 13, 18, 14, 2, 18, 14, 19, 13, 11, 8, 6, 6, 4, 2, 0, 3, 1, 0, 0, 0]))
print()