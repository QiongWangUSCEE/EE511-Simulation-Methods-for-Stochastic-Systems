import numpy as np
from scipy.special import comb


state = [0.5] + [0] * 199 + [0.5]
state = np.mat(state)
p = [[0] * 201 for i in range(201)]
for i in range(201):
    for j in range(201):
        p[i][j] = comb(200, j) * (i / (200)) ** j * (1 - i / (200)) ** (200 - j)
p = np.mat(p)
for i in range(1000):
    state *= p

for ele in state:
    print(ele)


