import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

x = np.linspace(-5, 5, 100)
y = 0.4 * np.array(norm(-1, 1).pdf(x)) + 0.6 * np.array(norm(1, 1).pdf(x))
p = 0.6
res = []
for i in range(10000):
    if np.random.rand() < p:
        res.append(np.random.normal(1,1))
    else:
        res.append(np.random.normal(-1,1))
plt.figure()
plt.hist(res, bins=50, density=1, label='simulation', color='b')
plt.plot(x, y.tolist(), label='theoretical', color='r')
plt.legend()
plt.show()

