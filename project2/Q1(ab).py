import numpy as np
import matplotlib.pyplot as plt

number_samples = 5000
outcomes = []
width = [1, 0.5, 0.2, 0.1]
for i in range(number_samples):
    outcomes.append(np.random.uniform(-3, 2))
plt.figure(1)
plt.title('histogram of outcome')
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.hist(outcomes, bins=np.arange(-3, 3, width[i]), edgecolor='black')
    plt.xticks(range(-3, 3))
    plt.xlabel('Sample Range')
    plt.ylabel('Sample Frequency')
plt.show()

print('Sample Mean:', np.mean(outcomes))
print('Sample Variance:', np.var(outcomes, ddof=1))
