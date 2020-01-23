# Name: Gabriel Barney
# Asgn: 3
# Sect: CSC-349-01

import sys

def main():

    fp_read = open(sys.argv[1], "r")
    lines = fp_read.read().strip("(").strip(")").strip(",").split()
    fp_read.close()

    times = []
    t = []
    triple = []
    str_num = ""

    for i in range(len(lines)):
        if (i % 2) != 0:
            times.append(lines[i])

    for i in times:
        for j in i:
            if j in "1234567890":
                str_num += j
            if j == ",":
                triple.append(int(str_num))
                str_num = ""

            if j == ")":
                triple.append(int(str_num))
                str_num = ""
                t.append(triple)
                triple = []

    sorted_t = sorted(t, key=sum)[::-1]
    duration_sum = 0

 
    if len(sorted_t) > 1:
        last_one = sum(sorted_t[-1])
        second_last = sum(sorted_t[-2])
        last_two = last_one / second_last

        if last_two <= 0.5:
            for i in range(0, len(sorted_t) - 2):
                duration_sum += sorted_t[i][0]
            duration_sum += sum(sorted_t[-2])
        else:
            for i in range(0, len(sorted_t) - 1):
                duration_sum +=  sorted_t[i][0]
            duration_sum += sum(sorted_t[-1])
    else:
        duration_sum += sum(sorted_t[0])

    order = []
    for i in sorted_t:
        for j in range(len(t)):

            if i == t[j]:
                order.append(j + 1)

    sequence = ""
    for i in order:
        sequence += str(i) + ","

    print("sequence: {0}".format(sequence[:-1]))
    print("completion time: {0}".format(duration_sum))


if __name__ == "__main__":
    main()
