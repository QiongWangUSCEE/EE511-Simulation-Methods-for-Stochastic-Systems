import random as rd
import matplotlib.pyplot as plt

# using a list to save the result of each toss, 0: Tail 1: Head
result = []
# toss 50 times
for i in range(100):
    # using generate 0 or 1 with equal probability
    result.append(int(rd.random()+0.5))

# record the run of head
run_of_head = []
# record the length of each consequent head
counter = 0
for ele in result:
    if ele:
        counter += 1
    elif counter:
        run_of_head.append(counter)
        counter = 0
if counter:
    run_of_head.append(counter)

plt.figure()
plt.hist(run_of_head, bins=range(max(run_of_head)+2), rwidth=0.8, edgecolor='black', align='left')
plt.xticks(range(max(run_of_head)+2))
plt.xlabel('Run of Head')
plt.ylabel('Frequency')
plt.title('100 times of fair Bernoulli trials')
plt.show()