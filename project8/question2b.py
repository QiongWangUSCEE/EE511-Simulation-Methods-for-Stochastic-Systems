import random
import numpy as np


dim = list(range(3))
for times in range(10):
    x = [[0.01] for i in range(3)]
    for i in range(10000):
        s, tmp = 0, 0
        r = random.randint(0, 2)
        for j in dim:
            if j == r:
                continue
            s += (j+1)*x[j][-1]
        rest = 1 - s
        while tmp * (r+1) >= rest:
            tmp = np.random.exponential(1)
        x[r].append(tmp)
    print(np.mean(x[0]+2*np.mean(x[1])+3*np.mean(x[2])))