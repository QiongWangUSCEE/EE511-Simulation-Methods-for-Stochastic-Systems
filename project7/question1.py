import numpy as np


mu = np.array([1, 2, 3])
sigma = np.array([[3, -1, 1], [-1, 5, 3], [1, 3, 4]])

A = np.linalg.cholesky(sigma)
for i in range(10):
    Z = np.array(np.random.rand(3))
    X = np.dot(A, Z.T) + mu
    print(X)
