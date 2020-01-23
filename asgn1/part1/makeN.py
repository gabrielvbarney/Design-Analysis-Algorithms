def makeN():
    fp_open = open("n.txt", "w")
    i = 10000
    while i <= 20000:
        fp_open.write(str(i))
        fp_open.write("\n")
        i += 20
    fp_open.close()
   
makeN() 
