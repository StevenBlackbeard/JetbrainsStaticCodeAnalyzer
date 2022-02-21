n = int(input())
# n = 3
# Define a generator squares that produces an infinite sequence of the squares
# of all natural numbers (1, 4, 9, 16, ...).
# For a given number n, print out the first n elements each on a new line.

def squares():
    i = 1
    while i <= n:
        yield i * i
        i += 1

# Don't forget to print out the first n numbers one by one here
output = squares()
for _ in range(n):
    print(next(output))
