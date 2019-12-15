import numpy as np


def main():
    for trial in range(10):
        print('# ' + str(trial) + ' trials:', run(10))


def run(n):
    ans = []
    for i in range(n):
        break_time = []
        arrival_time = arrive_list()
        time_ptr = 0
        while len(arrival_time):
            if time_ptr < arrival_time[0]:
                break_time.append(0.3 * np.random.rand())
                time_ptr += break_time[-1]
            else:
                time_ptr += np.random.exponential(1 / 25, 1)
                arrival_time.remove(arrival_time[0])
        ans.append(sum(break_time))
    return np.mean(ans)


def arrive_list():
    arrive_time = []
    rate = [x for x in range(4, 20, 3)] + [x for x in range(19, 6, -3)]
    for hour in range(100):
        time = hour
        while True:
            time += (-1/rate[hour % 10]) * np.log(np.random.uniform())
            if time - hour > 1:
                break
            arrive_time.append(time)
    return arrive_time


if __name__ == '__main__':
    main()