# Name: Gabriel Barney
# Asgn: 1
# Sect: CSC-349-01

import sys

def main():
    fp_open = open(sys.argv[1], "r")
    contents = fp_open.read().strip().split(", ")
    aList = [int(i) for i in contents]
    result = aSearcher(aList, 0, (len(aList) - 1))
    print(str(result))

def aSearcher(aList, aMin, aMax):
    mp = (aMin + aMax) // 2
    if aMax <= aMin:
        if aMax == aMin:
            return aList[aMax]
        return None
    if (mp % 2) == 0:
        if aList[mp + 1] == aList[mp]:
            # Lone element at higher index.
            return aSearcher(aList, (mp + 2), aMax)
        else:
            # Lone element at lower index.
            return aSearcher(aList, aMin, mp) 
    else:
        if aList[mp - 1] == aList[mp]:
            # Lone element at higher index.
            return aSearcher(aList, (mp + 1), aMax)
        else:
            # Lone element at lower index.
            return aSearcher(aList, aMin, (mp - 1))

if __name__ == "__main__":
    main()
