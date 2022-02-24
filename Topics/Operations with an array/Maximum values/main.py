import numpy as np

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
output = np.array([num_1, num_2, num_3])
print(np.max(output))
print(np.argmax(output))