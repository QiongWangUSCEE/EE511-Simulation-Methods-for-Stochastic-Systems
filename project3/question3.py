import numpy as np
import matplotlib.pyplot as plt


def main():
    sample_size = [100, 1000, 10000]
    for size in sample_size:
        samples = generate(size)
        plot_hist(samples, size)
        print('when using ' + str(size) + 'samples, E[N] =', np.mean(samples))
    plt.show()


def generate(size: int) -> list:
    result = []
    for i in range(size):
        N = 0
        counter = 0
        while N <= 4:
            N += np.random.uniform(0, 1)
            counter += 1
        result.append(counter)
    return result


def plot_hist(samples: list, size: int):
    plt.figure(size)
    plt.hist(samples, bins=range(min(samples) - 1, max(samples) + 2), rwidth=0.8, edgecolor='black', align='left')
    plt.xlabel('value of N')
    plt.ylabel('count of N')
    plt.title('histogram for values of N when ' + str(size) + ' samples')


if __name__ == '__main__':
    main()