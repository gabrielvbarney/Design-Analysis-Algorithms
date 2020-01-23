# Name: Gabriel Barney
# Asgn: 1
# Sect: CSC-349-01

import time
import random
import mergeSort as ms
import selectionSort as ss

def start():
    sample = [(1000, 2), (1200, 3)]
    merge_open = open("mergeStats.txt", "w")
    for i in sample:
        merge_open.write(str(i[0]))
        merge_open.write(" ")
    merge_open.close()
    mergeTimes = []
    selectTimes = []    
    n = 10000
    while n <= 20000:
        aList = []
        for i in range(n):
            aList.append(random.randint(-10000, 10000))
        aList_copy = aList
        mergeTimes = runTimeMerge(aList, n, mergeTimes)
        selectTimes = runTimeSelect(aList_copy, n, selectTimes)
        n += 20
    merge_open = open("mergeStats.txt", "w")
    select_open = open("selectStats.txt", "w")
    for i in mergeTimes:
        merge_open.write(str(i[0]))
    for i in selectTimes:
        select_open.write(str(i[0]))
    merge_open.close()
    select_open.close()

def runTimeMerge(aList, n, mergeTimes):
    start = time.time()
    mergeL = ms.merge_sort(aList)
    end = time.time()
    mergeTimes.append(((end-start),n))
    print("{0} elements in list".format(n))
    print("Merge Sort: {:.10f} seconds".format(end - start))
    return mergeTimes

def runTimeSelect(aList, n, selectTimes):
    start = time.time()
    selectionL = ss.selectionSort(aList)
    end = time.time()
    selectTimes.append(((end-start),n))
    print("Selection Sort: {:.10f} seconds\n".format(end - start))
    return selectTimes

start()
