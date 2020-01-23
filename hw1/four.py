def sameIndex(aMin, aMax, aList):
    print("aMax: {0}".format(aMax))
    print("aMin: {0}".format(aMin))
    if aMax <= aMin:
        if aList[aMax] != aMax:
            print("False")
            return False
    else:
        if aList[(aMax + aMin) // 2] > ((aMax + aMin) // 2):
            return sameIndex(aMin, ((aMax + aMin) // 2), aList)
        elif aList[(aMax + aMin) // 2] < ((aMax + aMin) // 2):
            return sameIndex(((aMax + aMin) // 2), aMax, aList)
        else:
            print("True")
            return True

sameIndex(0, 5, [19, 4, 94, 59, 23, 43]) 
sameIndex(0, 9, [0, 2, 3, 4, 5, 6, 7, 8, 9, 10])
