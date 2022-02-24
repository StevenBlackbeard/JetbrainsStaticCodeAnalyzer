import numpy as np

array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)

in_1 = int(input())
in_2 = int(input())
print(array[in_1].astype(np.str))
print(array[in_2].astype(np.float64))
