# Name: Gabriel Barney
# Asgn: 1
# Sect: CSC-349-01

def selectionSort(aList):
    listLength = len(aList) - 1
    big_i = None
    for i in range(len(aList)-1, -1, -1):
        for j in range(0, listLength):
            if big_i != None:
                if aList[j] > aList[big_i]:
                    big_i = j
            else:
                if aList[j] > aList[i]:
                    big_i = j 
        if big_i != None:
            temp = aList[i]
            aList[i] = aList[big_i]
            aList[big_i] = temp
        big_i = None
        listLength -= 1
    return aList
