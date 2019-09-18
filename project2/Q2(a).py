import random
import numpy as np

X = []
X_k = []
X_k1 = []

length_k = 1000

for i in range(length_k + 1):
    X.append(random.uniform(0, 1))

X_k = X[:length_k]
X_k1 = X[1:]

print(np.cov([X_k, X_k1]))
