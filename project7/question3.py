import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

covariance_type = ['full', 'tied', 'diag', 'spherical']
cov1 = np.mat("0 0.3;0.1 0")
cov2 = np.mat("0 0.2;0.3 0")
mu1 = np.array([0, 1])
mu2 = np.array([2, 1])

X = np.zeros((300, 2))
l1 = [1]*100+[0]*200
l2 = [0]*100+[1]*200
X[:100, :] = np.random.multivariate_normal(mean=mu1, cov=cov1, size=100)
X[100:, :] = np.random.multivariate_normal(mean=mu2, cov=cov2, size=200)
plt.figure(dpi=500, figsize=[12,9])
subfigure = 1
for method in covariance_type:
    start = time.time()
    gmm = GaussianMixture(n_components=2, covariance_type=method)
    gmm.fit(X)
    y = gmm.predict(X)
    labels = gmm.predict(X)
    end = time.time()
    print()
    print('covariance_type:', method)
    print('weight:', gmm.weights_[0])
    print('weight error:', min(abs(gmm.weights_[0]-0.666667)/0.666667, abs(gmm.weights_[0]-0.333333)/0.333333))
    print('mean:\n', gmm.means_, '\n')
    print('covariance:\n', gmm.covariances_, '\n')
    print('accurcy:', max(np.mean(l1 == labels), np.mean(l2 == labels)))
    print('run time:', end-start)
    plt.subplot(2,2,subfigure)
    subfigure += 1
    plt.title(method)
    plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis');
plt.show()