import numpy as np

numbers = [int(input()) for _ in range(6)]
a = np.reshape(numbers[:4], (2, 2))
v = np.array(numbers[4:])
print(a @ v)
