import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = np.array([a, b, c, d])
print(arr[np.where(arr >= 45)])
