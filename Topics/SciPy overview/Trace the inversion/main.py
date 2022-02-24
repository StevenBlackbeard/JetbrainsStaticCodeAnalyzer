import numpy
from numpy.linalg import inv

A = numpy.array([[1, 2], [2, 3]])

# your code
inv_a = inv(A)
print(numpy.trace(inv_a))