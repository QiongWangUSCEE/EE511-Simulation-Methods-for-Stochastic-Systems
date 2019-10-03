import random
import math
import numpy as np


def main():
    waiting = read_txt('faithful.dat.txt')

    run_15_data(waiting[:15])

    run_all_data(waiting)


def run_15_data(data_set):
    print('95% statistical confidence for 15 data:')
    lower, upper = statistical(data_set)
    print('lower bound:', lower)
    print('upper bound:', upper)
    print('')

    print('95% bootstrap confidence for 15 data:')
    lower, upper = bootstrap(data_set)
    print('lower bound:', lower)
    print('upper bound:', upper)
    print('')


def run_all_data(data_set):
    print('95% statistical confidence for all data:')
    lower, upper = statistical(data_set)
    print('lower bound:', lower)
    print('upper bound:', upper)
    print('')

    print('95% bootstrap confidence for all data:')
    lower, upper = bootstrap(data_set)
    print('lower bound:', lower)
    print('upper bound:', upper)
    print('')


def statistical(data_set):
    mean = np.mean(data_set)
    std = np.std(data_set, ddof=1)
    z = 1.96
    return [mean-z*(std/math.sqrt(len(data_set))), mean+z*(std/math.sqrt(len(data_set)))]


def bootstrap(data_set):
    length = len(data_set)
    result = []
    for i in range(10000):
        candidate = []
        for j in range(length):
            candidate.append(random.sample(data_set, 1))
        result.append(np.mean(candidate))
    return [np.percentile(result, 2.5), np.percentile(result, 97.5)]


def read_txt(address):
    with open(address, 'r') as f:
        data = f.readlines()

    line = 0
    while data[line][0] != '1':
        line += 1

    waiting = []

    for i in range(line, line + 272):
        waiting.append(int(data[i].split()[-1]))

    return waiting


if __name__ == '__main__':
    main()