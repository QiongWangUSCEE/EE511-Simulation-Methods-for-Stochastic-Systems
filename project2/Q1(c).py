import random
import numpy as np
import matplotlib.pyplot as plt

std = []
mean = []
samples = []
number_samples = 50
number_resample = 10000

for i in range(number_samples):
    samples.append(np.random.uniform(-3, 2))

for i in range(number_resample):
    resample = []
    for j in range(number_samples):
        resample.append(random.sample(samples, 1))
    std.append(np.std(resample, ddof=1))
    mean.append(np.mean(resample))

plt.figure(1)
plt.subplot(2, 1, 1)
plt.title('mean')
plt.hist(mean, bins=np.arange(min(mean) - 0.1, max(mean) + 0.2, 0.05), edgecolor='black')

plt.subplot(2, 1, 2)
plt.title('std')
plt.hist(std, bins=np.arange(min(std) - 0.1, max(std) + 0.2, 0.02), edgecolor='black')

plt.show()

mean.sort()
std.sort()
print('2.5% mean:', mean[249])
print('97.5% mean:', mean[9749])
print('2.5% std:', std[249])
print('97.5% std:', std[9749])
