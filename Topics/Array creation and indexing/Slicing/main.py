import numpy as np


a = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
              [[30, 31, 32], [33, 34, 35], [36, 37, 38]],
              [[40, 41, 42], [43, 44, 45], [46, 47, 48]],
              [[50, 51, 52], [53, 54, 55], [56, 57, 58]],
              [[60, 61, 62], [63, 64, 65], [66, 67, 68]],
              [[70, 71, 62], [73, 74, 65], [76, 77, 78]],
              [[80, 81, 62], [83, 84, 85], [86, 87, 88]]])
# your code here
in_1 = int(input())
in_2 = int(input())
in_3 = int(input())

# b = a[::in_1]
# c = b[:, ::in_2, ]
# print(c[:, :, in_3])

print(a[::in_1, ::in_2, in_3])


