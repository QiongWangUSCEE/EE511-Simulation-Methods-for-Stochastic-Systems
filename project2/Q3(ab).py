import random
import matplotlib.pyplot as plt

for times in range(20):
    X2 = 0
    num = 1000
    degree = 9
    sample = []
    for i in range(num):
        sample.extend(random.sample(range(10), 1))
    for i in range(degree + 1):
        X2 += ((sample.count(i) - num / (degree + 1)) ** 2) / (num / (degree + 1))
    print('In the ' + str(times) + ' times calculation, chi-Square =', X2)

plt.figure()
plt.hist(sample, bins=range(11), edgecolor='black', )
plt.xlabel('value of samples')
plt.ylabel('number of sample')
plt.show()
