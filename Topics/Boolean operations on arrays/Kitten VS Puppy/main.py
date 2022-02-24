import numpy as np

lst_1 = []
for i in input().split():
    lst_1.append(int(i))
lst_2 = input().split()
lst_3 = input().split()

# finish the code here, help the Kitten and the Puppy!
out = np.where(np.array(lst_1) >= 0, np.array(lst_2), np.array(lst_3))
for i in out:
    print(i)