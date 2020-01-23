# Name: Gabriel Barney
# Sect: CSC-349-01
# Asgn: 4

import sys

def main():
    fp_read = open(sys.argv[1], "r")
    lines = fp_read.readlines()
    scoring = []
    score = 0
    x = [i for i in lines[0] if i != "\n"]
    y = [i for i in lines[1] if i != "\n"]
    print(x)
    print(y)
    return
    lines = lines[2:]
    row = []
    for i in lines:
        i = i.strip().split()
        for j in i:
            row.append(j)
        scoring.append(row)
        row = []
    fp_read.close()
    post_x = []
    post_y = []
    dynamic(scoring, score, x, y, post_x, post_y)

def dynamic(scoring, score, x, y, post_x, post_y):
    if (len(x) == 0) or (len(y) == 0):
        if len(x) == 0:
            for i in y:
                post_y.append(i)
                post_x.append("-")
        else:
            for i in x:
                post_x.append(i)
                post_y.append("-")
        the_x = ""
        the_y = ""
        for i in post_x:
            the_x += i + " "
        for i in post_y:
            the_y += i + " "
        print("x: {0}".format(the_x[:-1]))
        print("y: {0}".format(the_y[:-1]))
        print("Score: {0}".format(score))        
        return None
            
    if len(x) > len(y):
        used = x[0]
        other = y[0]
        used_arr = "x"
    else:
        used = y[0]
        other = x[0]
        used_arr = "y"
    
    col = 0                 # potentially have to redo
    breaker = False
    for i in scoring:
        for j in i:
            if j == used:
                breaker = True
                break
            col += 1
        if breaker == True:
            break
    row = 0
    breaker = False
    for i in scoring:
        for j in i: 
            if j == other:
                breaker = True
                break
            row += 1
        if breaker == True:
            break
    
    match_val = scoring[row][col] # look at this
    if scoring[0][col] == used:
        gap_val = scoring[5][col] 
    else:
        gap_val = scoring[5][row]
    no_gap = False
    a_gap = False
   
    xG = False
    yG = False


 
    if (int(match_val)-1 > int(gap_val)) and ((x[0] != "C" and y[0] != "G") and (x[0] != "G" and y[0] != "C")):
        score += int(match_val)
        no_gap = True

    if x[0] == "G" and y[0] == "C":
        score += int(gap_val)
        a_gap = True
        xG = True
        print("xG", x[0], y[0])
    if y[0] == "G" and x[0] == "C":
        score += int(gap_val)
        a_gap = True
        yG = True
        print("yG", x[0], y[0])
            
    
    elif (int(gap_val) >= int(match_val)-1):
        score += int(gap_val)
        a_gap = True
    
    


    if x[0] == "G" and y[0] == "T":
        print(len(x), len(y))
        print("xG", "yT")


    if used != other:
        
        if used_arr == "x":
            if no_gap == True:
                post_x.append(used)
                post_y.append(other)
                x = x[1:]
                y = y[1:]
            elif a_gap == True:
                post_x.append(used)
                post_y.append("-")
                x = x[1:]
        elif used_arr == "y":
            if no_gap == True:
                post_y.append(used)
                post_x.append(other)
                x = x[1:]
                y = y[1:]
            elif a_gap == True:
                post_y.append(used)
                post_x.append("-")
                y = y[1:]
    


    elif used == other:
        score += int(scoring[row][col])
        post_x.append(used)
        post_y.append(other)
        x = x[1:]
        y = y[1:]
    no_gap = False
    a_gap = False

    return dynamic(scoring, score, x, y, post_x, post_y)


if __name__ == "__main__":
    main()
