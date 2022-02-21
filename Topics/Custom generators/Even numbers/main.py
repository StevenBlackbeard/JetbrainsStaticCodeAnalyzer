n = int(input())


def even():
    i = 0
    while i <= n:
        yield i * 2
        i += 1


# Don't forget to print out the first n numbers one by one here
output = even()
for _ in range(n):
    print(next(output))

