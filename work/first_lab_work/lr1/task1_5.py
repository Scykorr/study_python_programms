import numpy

M1 = numpy.array([[9., 6., 3., 8.], [4., 6., 7., 4.], [2., 3., 5., 3.], [4., 8., 3., 7.]])
v1 = numpy.array([3., 1., 4., 2.])
print(numpy.linalg.solve(M1, v1))
