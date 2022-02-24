import numpy as np

# list_in = []
# for i in range(6):
#     list_in.append(int(input()))
#
# arr = np.array([list_in[0:2], list_in[2:4]])
# vec = np.array(list_in[4:6])
#
# print(np.transpose(np.divide(arr, vec)))

numbers = [int(input()) for _ in range(6)]
a = np.reshape(numbers[:4], (2, 2))
v = np.array(numbers[4:])
print((a / v).T)