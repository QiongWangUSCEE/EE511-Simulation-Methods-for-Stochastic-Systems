import random
import matplotlib.pyplot as plt


def main():
    reject_prob = []
    for i in range(500, 10500, 500):
        reject_prob.append(100 * count_defective(i, 5) / i)
        print('reject probability for '+str(i)+' times trials', str(reject_prob[-1]) + '%')

    plt.figure()
    plt.scatter([x for x in range(500, 10500, 500)], reject_prob, label='reject probability', color='red')
    plt.plot([x for x in range(500, 10500, 500)], [22.13]*20, label='theoretical value: 22.13%', linestyle='-')
    plt.xlabel('trial times')
    plt.ylabel('reject probability %')
    plt.legend()
    plt.show()

    for i in range(10):
        for index in range(126):
            if count_defective(1000, index) >= 950:
                print('the fewest number:', index)
                break


def count_defective(check_times: int, check_threshold) -> int:
    result = 0
    for times in range(check_times):
        lot = [x for x in range(1, 126)]
        flag = True
        for i in range(check_threshold):
            test = random.sample(lot, 1)[0]
            if test < 7:
                flag = False
                break
            lot.remove(test)

        if not flag:
            result += 1

    return result


if __name__ == '__main__':
    main()
