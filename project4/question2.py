import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt


for n in [10, 100, 1000]:
    sample = []
    for i in range(n):
        z1 = np.random.standard_normal()
        z2 = np.random.standard_normal()
        z3 = np.random.standard_normal()
        z4 = np.random.standard_normal()
        sample.append(z1 ** 2 + z2 ** 2 + z3 ** 2 + z4 ** 2)
    x_cdf = sm.distributions.ECDF(sample)
    x_line = np.linspace(min(sample), max(sample))
    cdf = stats.chi2.cdf(x_line, df=4)
    plt.figure()
    plt.title('When n = ' + str(n) + ' Empirical CDF Figure')
    plt.step(x_line, x_cdf(x_line), label='Empirical CDF')
    plt.plot(x_line, cdf, label='Theoretical CDF')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

    print('When n =', n)
    print('maximum difference =', max([abs(list(cdf.data)[k]-x_cdf(x_line)[k]) for k in range(len(x_cdf(x_line)))]))
    print('Empirical 25% percentiles =', np.percentile(x_cdf(x_line), 25))
    print('Theoretical 25% percentiles =', np.percentile(list(cdf.data), 25))
    print('Empirical 50% percentiles =', np.percentile(x_cdf(x_line), 50))
    print('Theoretical 50% percentiles =', np.percentile(list(cdf.data), 50))
    print('Empirical 90% percentiles =', np.percentile(x_cdf(x_line), 90))
    print('Theoretical 90% percentiles =', np.percentile(list(cdf.data), 90))
    print('')