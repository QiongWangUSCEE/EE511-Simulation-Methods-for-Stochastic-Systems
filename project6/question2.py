import numpy as np
import math
import matplotlib.pyplot as plt


def main():
    N = 100000
    ans = []
    accept = 0
    theoretical = []
    for i in range(N):
        u1 = np.random.uniform()
        u1 = -5.5 * np.log(u1)
        if np.random.uniform() < f(u1, 5.5, 1) / (np.e * g(u1)):
            accept += 1
            ans.append(u1)

    x = np.arange(0, 40, 0.5)
    for ele in x:
        theoretical.append(f(ele, 5.5, 1))

    print('acceptance rate:', accept/N)

    plt.figure()
    plt.hist(ans, bins=40, edgecolor='black', label='simulation', density=1)
    plt.plot(x, theoretical, color='r', label='theoretical')
    plt.legend()
    plt.show()


def f(x, a, b):
    return (x ** (a - 1)) * ((1 / b) ** a) * (np.exp(-x / b)) / ((math.pi ** 0.5) * 1 * 3 * 5 * 7 * 9/(2**5))


def g(x):
    return (2/11)*np.exp(-2*x/11)


if __name__ == '__main__':
    main()