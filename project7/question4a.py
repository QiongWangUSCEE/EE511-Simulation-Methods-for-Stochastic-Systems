from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

with open('faithful.dat.txt', 'r') as f:
    data = f.readlines()

line = 0
while data[line][0] != '1':
    line += 1

waiting = []
eruptions = []
raw = []

for i in range(line, line + 272):
    eruptions.append(float(data[i].split()[-2]))
    waiting.append(int(data[i].split()[-1]))
    raw.append([eruptions[-1], waiting[-1]])

plt.figure(1)
plt.scatter(eruptions, waiting)
plt.xlabel('eruptions')
plt.ylabel('waiting')

plt.figure(2)
plt.scatter(eruptions, waiting)
plt.xlabel('eruptions')
plt.ylabel('waiting')
kmeans = KMeans(n_clusters=2)
kmeans.fit(raw)
plt.plot(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 'ro')

plt.figure(3)
colors = ['b', 'r']
for i,l in enumerate(kmeans.labels_):
     plt.plot(eruptions[i],waiting[i],color=colors[l],marker='o',ls='None')

plt.show()