import random
import numpy as np

X = [0, 0, 0]
X_k = []
Y_k = []

length_k = 1000

for i in range(length_k):
    X.append(random.uniform(0, 1))

for i in range(3, length_k + 3):
    X_k.append(X[i])
    Y_k.append(X[i] - 2 * X[i - 1] + 0.5 * X[i - 2] - X[i - 3])

print(np.cov([X_k, Y_k]))
