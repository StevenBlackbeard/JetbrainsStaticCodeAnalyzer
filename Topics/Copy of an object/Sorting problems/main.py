import copy

# sorting function
def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# where copying takes place
arr = [int(i) for i in input().split()]
arr_copy = copy.copy(arr)
sorted_arr = bubble_sort(arr)

if arr_copy == sorted_arr:
    print('sorted')
else:
    print('not sorted')

# other
# arr = [int(i) for i in input().split()]
# sorted_arr = bubble_sort(arr[:])
#
# if arr_copy == sorted_arr:
#     print('sorted')
# else:
#     print('not sorted')

