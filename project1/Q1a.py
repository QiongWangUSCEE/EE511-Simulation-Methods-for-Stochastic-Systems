import random as rd
import matplotlib.pyplot as plt


def main():
    # get the dataset for different number times of Bernoulli trial (n=50, p=0.5)
    result20 = experiment(20)
    result100 = experiment(100)
    result200 = experiment(200)
    result1000 = experiment(1000)
    result2000 = experiment(2000)
    result10000 = experiment(10000)

    # set the size of the figure, and plot 6 histograms
    plt.rcParams['figure.figsize'] = (24, 18)
    plt.rcParams['savefig.dpi'] = 300
    plt.figure()

    result = [result20, result100, result200, result1000, result2000, result10000]
    times = [20, 100, 200, 1000, 2000, 10000]
    for i in range(1, 7):
        plt.subplot(3, 2, i)
        plt.hist(result[i - 1], bins=range(50), rwidth=1, edgecolor='black', align='left')
        plt.title(str(times[i - 1]) + ' times')
        plt.xlabel('Number of Heads')
        plt.ylabel('Frequency')

    plt.show()


# return the number of heads for each Bernoulli trial (n=50, p=0.5)
def experiment(times: int) -> list:
    result = []
    for j in range(times):
        head = 0
        for i in range(50):
            head += int(rd.random() + 0.5)
        result.append(head)
    return result


if __name__ == '__main__':
    main()
