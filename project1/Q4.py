import random as rd
import matplotlib.pyplot as plt


def main():
    result = []
    # set the user‐specified positive number
    threshold = range(1, 30)
    for ele in threshold:
        result.append(toss_to_special_number_of_head(ele))
    print(result)

    plt.figure()
    plt.plot(threshold, result, color='red',marker='o', label='Simulation')
    plt.plot(threshold, range(2, 60, 2), ls=':', label='y=2x')
    plt.xlabel('Target Number')
    plt.ylabel('Toss Times')
    plt.legend()
    plt.show()


# count the number of tosses until reaching a user‐specified positive number of heads
def toss_to_special_number_of_head(number: int) -> int:
    tossing_times = 0
    counter = 0
    # toss a coin continually
    while True:
        tossing_times += 1
        counter += int(rd.random()+0.5)
        # reach the user‐specified positive number
        if counter == number:
            return tossing_times


if __name__ == '__main__':
    main()
