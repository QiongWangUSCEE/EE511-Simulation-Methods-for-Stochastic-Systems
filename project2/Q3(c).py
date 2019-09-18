import random

for times in range(20):
    X2 = 0
    num = 1000
    degree = 9
    sample = []
    for i in range(num):
        sample.extend(random.sample(range(10), 1))
    X2 += ((sample.count(0) + sample.count(1) - num / (degree + 1)) ** 2) / (num / (degree + 1))
    for i in range(2, degree + 2):
        X2 += ((sample.count(i) - num / (degree + 1)) ** 2) / (num / (degree + 1))
    print('In the ' + str(times) + ' times calculation, chi-Square =', X2)
