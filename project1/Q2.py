import random as rd
import matplotlib.pyplot as plt

# using a list to save the result of each toss, 0: Tail 1: Head
result = []
# toss 200 times
for i in range(200):
    # using generate 0 or 1 p(1)=0.8 p(0)=0.2
    result.append(int(rd.random()+0.8))

# record the longest run of head
longest_run_of_head = 0
# record the length of each consequent head
counter = 0
for ele in result:
    if ele:
        counter += 1
    else:
        # compare each length of consequent head with the previous longest run of head
        longest_run_of_head = max(longest_run_of_head,counter)
        counter = 0
longest_run_of_head = max(longest_run_of_head,counter)
# print result
print('Longest Run of Head:', longest_run_of_head)
print('Number of Head:', result.count(1))

# Calculate the frequency of appearance of the Head and Tail after toss
# number of Heads
sum = 0
# frequency of appearance of the Head
prob_head = []
# frequency of appearance of the Tail
prob_tail = []
toss_times = 0
for ele in result:
    toss_times += 1
    if ele:
        sum += 1
    # frequency of appearance
    prob_head.append(sum/toss_times)
    prob_tail.append(1-sum/toss_times)

# plot a line chart and histogram
plt.figure()

plt.subplot(1,2,1)
plt.hist(result, bins=range(3), rwidth=0.8, edgecolor='black', align='left')
plt.xticks(range(3))
plt.xlabel('1:Head 0:Tail')
plt.ylabel('Frequency')
plt.title('Bernoulli Outcomes')

plt.subplot(1,2,2)
plt.plot(range(1,toss_times+1), prob_head, color='green', label='Frequency of Head')
plt.plot(range(1,toss_times+1), prob_tail, color='red', label='Frequency of Tail')
plt.xlabel('Toss Times')
plt.ylabel('Frequency')
plt.title('Changing of Frequency')
plt.legend()

plt.show()
