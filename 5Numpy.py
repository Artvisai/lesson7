import numpy

matrix = numpy.random.randint(-100, 100, (3, 3))
print("Before:")
print(matrix)
print("After:")
print(matrix.transpose())
