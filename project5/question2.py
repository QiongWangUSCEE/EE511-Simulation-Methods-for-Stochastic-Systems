import numpy as np
import matplotlib.pyplot as plt


def main():
    r = [0.75, 0.25]
    ans_buffer1 = []
    ans_buffer2 = []
    ans_output1 = []
    ans_output2 = []
    for p in np.arange(0.01,1,0.01):
        buffer1 = 0
        buffer2 = 0
        output1 = 0
        output2 = 0
        for times in range(1000):
            if buffer1 and buffer2:
                choose1 = np.random.uniform()
                choose2 = np.random.uniform()

                if choose1 < r[0] and choose2 < r[0]:
                    output1 += 1
                    if np.random.uniform() < 0.5:
                        buffer1 -= 1
                    else:
                        buffer2 -= 1

                elif choose1 >= r[0] and choose2 >= r[0]:
                    output2 += 1
                    if np.random.uniform() < 0.5:
                        buffer1 -= 1
                    else:
                        buffer2 -= 1

                else:
                    output1 += 1
                    output2 += 1
                    buffer1 -= 1
                    buffer2 -= 1

            elif buffer1:
                buffer1 -= 1
                if np.random.uniform() < r[0]:
                    output1 += 1
                else:
                    output2 += 1

            elif buffer2:
                buffer2 -= 1
                if np.random.uniform() < r[0]:
                    output1 += 1
                else:
                    output2 += 1

            if np.random.uniform() < p:
                buffer1 += 1
            if np.random.uniform() < p:
                buffer2 += 1
        ans_buffer1.append(buffer1)
        ans_buffer2.append(buffer2)
        ans_output1.append(output1/1000)
        ans_output2.append(output2/1000)

    plt.figure()
    plt.plot(np.arange(0.01,1,0.01), ans_output1)
    plt.xlabel('p')
    plt.ylabel('# packet per minute')

    plt.figure()
    plt.plot(np.arange(0.01, 1, 0.01), ans_output2)
    plt.xlabel('p')
    plt.ylabel('# packet per minute')
    plt.show()


if __name__ == '__main__':
    main()
