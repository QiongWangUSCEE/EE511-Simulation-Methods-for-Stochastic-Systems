import numpy as np
import matplotlib.pyplot as plt

accepted = []
p = [0.06]*5+[0.15, 0.13, 0.14, 0.15, 0.13]+[0]*10
q = [0.05]*20
c = 3
N = 10000

for i in range(N):
    j = np.random.randint(20)
    u = np.random.uniform(0, 1)
    if u < p[j]/(c*q[j]):
        accepted.append(j+1)

plt.figure()
plt.hist(accepted, bins=range(21), rwidth=0.8, edgecolor='black', align='left', label='Accept-Reject Sample')
plt.plot(range(1, 21), [x*N/c for x in p], marker='o', color='r', label='distribution pj')
plt.xlabel('Random Variable')
plt.ylabel('Frequency')
plt.title('Histogram for Distribution of p')
plt.legend()
plt.show()

print('sample mean =', np.mean(accepted))
print('sample variance =', np.var(accepted, ddof=1))
print('efficiency =', len(accepted)/N)