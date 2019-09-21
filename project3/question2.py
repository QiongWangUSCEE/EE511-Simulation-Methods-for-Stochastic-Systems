import numpy as np
import matplotlib.pyplot as plt


average = 120
N = 10000
p = average/N

poisson = []
prob = (average ** 79)*np.exp(-average)/np.math.factorial(79)
for i in range(16, 32):
    number = 0
    for j in range(5):
        x = 5*i+j
        prob *= (average/x)
        number += 1000 * prob
    poisson.append(int(number))


bernoulli_result = []
for i in range(1000):
    counter = 0
    for j in range(N):
        flip = np.random.uniform(0, 1)
        if flip <= p:
            counter += 1
    bernoulli_result.append(counter)

plt.figure(1)
plt.hist(bernoulli_result, bins=range(min(bernoulli_result) - 1, max(bernoulli_result) + 2, 5), rwidth=0.8, alpha=0.4, color='r', label='bernoulli trials',  align='left')
plt.plot(range(80, 160, 5), poisson, marker='o', color='b', label='theoretical')
plt.xlabel('Number of Cars')
plt.ylabel('Frequency')
plt.title('Histogram for using bernoulli trails')
plt.legend()

inv_transform_result = []
for times in range(1000):
    U = np.random.uniform(0, 1)
    i = 0
    P = np.exp(-average)
    F = P
    while 1:
        if U < F:
            inv_transform_result.append(i)
            break
        else:
            P = (average*P)/(i+1)
            F += P
            i += 1

plt.figure(2)
plt.hist(inv_transform_result, bins=range(min(inv_transform_result) - 1, max(inv_transform_result) + 2, 5), rwidth=0.8, alpha=0.4, color='r', label='inverse transform',  align='left')
plt.plot(range(80, 160, 5), poisson, marker='o', color='b', label='theoretical')
plt.xlabel('Number of Cars')
plt.ylabel('Frequency')
plt.title('Histogram for using inverse transform')
plt.legend()
plt.show()

