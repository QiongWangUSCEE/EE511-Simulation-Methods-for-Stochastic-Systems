import numpy as np
import matplotlib.pyplot as plt

s = 0
for i in range(1, 61):
    s += (1/i)
p = 1/s

result = []
for i in range(10000):
    counter = 0
    while True:
        flip = np.random.uniform(0, 1)
        counter += 1
        if flip < p/60:
            result.append(counter)
            break

print('E[N60] =', np.mean(result))
print('var[N60] =', np.var(result))

plt.figure()
plt.hist(result, bins=range(max(result)+1), rwidth=0.8, color='r', align='left')
plt.xlabel('Value of N60')
plt.ylabel('Frequency')
plt.title('Histogram for Distribution of N60')
plt.show()
