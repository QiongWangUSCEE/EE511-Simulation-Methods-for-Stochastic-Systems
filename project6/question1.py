import time
import math
import numpy as np
import matplotlib.pyplot as plt


def main():
    a, x, y = box_muller(1000)
    theoretical_pdf = theoretical(np.arange(min(a)-1, max(a)+2, 0.05))
    draw_pdf(a, theoretical_pdf)

    print('x y covariance:', np.cov(np.vstack((x,y))))
    print('sample mean:', np.mean(a))
    print('sample variance:', np.var(a, ddof=1))

    print_box_muller_time(1000000)
    print_polar_marsaglia_time(1000000)


def draw_pdf(a, theoretical_pdf):
    plt.figure()
    plt.hist(a, bins=math.ceil(max(a) - min(a)), edgecolor='black', label='Box Muller', density = 1)
    plt.plot(np.arange(min(a) - 1, max(a) + 2, 0.05), theoretical_pdf, color='r', label='theoretical')
    plt.xticks(range(int(min(a)) - 1, int(max(a)) + 2))
    plt.xlabel('A value')
    plt.ylabel('Sample Frequency')
    plt.legend()
    plt.show()


def box_muller(n):
    a = []
    x = []
    y = []
    for i in range(n):
        u1, u2 = np.random.uniform(size=2)
        _x = ((-2 * math.log(u1)) ** 0.5) * math.cos(2 * math.pi * u2)
        x.append(2 * _x + 1)
        _y = ((-2 * math.log(u1)) ** 0.5) * math.sin(2 * math.pi * u2)
        y.append(3 * _y + 2)
        a.append(2 * _x + 1 + 3 * _y + 2)
    return a, x, y


def polar_marsaglia(n):
    a = []
    counter = 0
    while counter < n:
        x, y = np.random.uniform(-1, 1, size=2)
        s = x ** 2 + y ** 2
        if s < 1:
            r1 = x * ((-2 * np.log(s) / s) ** 0.5)
            r2 = y * ((-2 * np.log(s) / s) ** 0.5)
            a.append(2 * r1 + 1 + 3 * r2 + 2)
            counter += 1
    return a


def theoretical(xrange):
    theoretical_pdf = []
    for x in xrange:
        theoretical_pdf.append(np.exp(-((x - 3) ** 2) / (2 * 13)) / ((13 ** 0.5) * np.sqrt(2 * np.pi)))
    return theoretical_pdf


def print_box_muller_time(n):
    box_muller_start = time.time()
    box_muller(1000000)
    box_muller_end = time.time()
    print('box muller time:', box_muller_end - box_muller_start)
    return


def print_polar_marsaglia_time(n):
    polar_marsaglia_start = time.time()
    polar_marsaglia(n)
    polar_marsaglia_end = time.time()
    print('polar marsaglia time:', polar_marsaglia_end - polar_marsaglia_start)
    return


if __name__ == '__main__':
    main()
