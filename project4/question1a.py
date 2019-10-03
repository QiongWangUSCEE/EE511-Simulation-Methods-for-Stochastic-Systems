import numpy as np

for times in range(20):
    result = []
    for i in range(10000):
        u = np.random.uniform()
        result.append(4*np.exp(16*(u**2)-12*u+2))
    print('simulation result =', np.mean(result))