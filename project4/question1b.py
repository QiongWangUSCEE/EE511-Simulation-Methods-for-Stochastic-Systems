import numpy as np

ans = []
for times in range(20):
    result = []
    for i in range(10000):
        u = np.random.uniform()
        result.append(2*(np.exp(-(1/u-1)**2)/u**2))
    print('simulation result =', np.mean(result))
    ans.append(np.mean(result))

print('maximum value =', max(ans))
print('minimum value =', min(ans))
print('mean of value =', np.mean(ans))
print('variance of value =', np.var(ans))
