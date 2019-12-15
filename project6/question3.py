import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import levy_stable


def main():
    a = [0.5, 1, 1.8, 2.0]
    b = [1, 0.75]
    fig = 1
    for _b in b:
        for _a in a:
            draw(_a, _b, fig)
            fig += 1
    plt.show()


def draw(a, b, fig):
    x = []
    for i in range(1000):
        w = np.random.exponential(1)
        x.append(F_inv(w, a, b))
    plt.figure(fig)
    plt.subplot(1,2,1)
    plt.hist(x, bins=100, color='r', label='a='+str(a)+' b='+str(b),rwidth=0.8, density=1)
    r = levy_stable.rvs(a, b, size=1000, scale=1)
    plt.hist(r, bins=100, label="Theoretical", color='b', rwidth=0.8, density=1)
    plt.title('Sample histogram')
    plt.legend()
    plt.subplot(1,2,2)
    plt.plot(np.arange(0,1000), x)
    plt.title('time series plot')
    return


def F_inv(w, a, b):
    gamma = np.random.uniform(-np.pi/2, np.pi/2)
    if a == 1:
        return (np.pi/2 + b*gamma)*math.tan(gamma)-b*np.log(w*math.cos(gamma)/(np.pi/2 + b*gamma))
    else:
        gamma_0 = (-np.pi/2)*b*K(a)/a
        return (math.sin(a*(gamma-gamma_0))/(math.cos(gamma)**(1/a))) * ((math.cos(gamma-a*(gamma-gamma_0))/w)**((1-a)/a))


def K(a):
    if a < 1:
        return a
    elif a > 1:
        return a-2


if __name__ == '__main__':
    main()