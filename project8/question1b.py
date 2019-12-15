import numpy as np


def my_func(x, y):
    return np.cos(np.pi + 5*x + 5*y)


N = 1000
fX = np.random.uniform(-1, 1, N)
fY = np.random.uniform(-1, 1, N)
X = my_func(fX, fY)
print('Mean is:', str(np.mean(X)))
print(2 * np.std(X) / np.sqrt(N))

# stratified sampling
K = 20
XSb = np.zeros((K, K))
SS = np.zeros_like(XSb)
Nij = N / np.power(K, 2)

for i in range(K):
    for j in range(K):
        XS = my_func((i + np.random.uniform(-1, 1, int(Nij))) / K, (j + np.random.uniform(-1, 1, int(Nij))) / K)
        XSb[i][j] = np.mean(XS)
        SS[i][j] = np.var(XS)

SST = np.mean((SS / N))
SSM = np.mean((XSb))
print('Mean with stratified sampling is:', str(SSM))
print(2 * np.sqrt(SST))

# importance sampling
N_is = 1000
U = 2 * np.random.rand(2, N_is) - 1
X_is = np.log(1 + U)
T = (np.e-1) ** 2 * np.cos(np.pi + 5 * X_is[0] + 5 * X_is[1] - (X_is[0] + X_is[1]))
print('Mean is:', str(np.mean(T)))
print(2 * np.std(T) / np.sqrt(N))
