# Name: Gabriel Barney
# Sect: CSC-349-01
# Asgn: 4

import sys

def main():
    fp_read = open(sys.argv[1], "r")
    lines = fp_read.readlines()
    scoring = []
    x = [i for i in lines[0] if i != "\n"]
    y = [i for i in lines[1] if i != "\n"]
    x.insert(0, "-")
    y.insert(0, "-")
    lines = lines[2:]
    row = []
    for i in lines:
        i = i.strip().split()
        for j in i:
            row.append(j)
        scoring.append(row)
        row = []
    fp_read.close()
    dyn_table = []
    while len(dyn_table) < (len(y)):
        rows = make_new_row(x)
        dyn_table.append(rows)
    dynamic_table = dynamic(scoring, x, y, dyn_table, 0, 0)
    traverse_table(x, y, dynamic_table, len(y) - 1, len(x) - 1, "", "", scoring)


def traverse_table(x, y, dynamic_table, row, col, x_str, y_str, scoring):
    while x != [] and y != []:

        x_val = x[col]
        y_val = y[row]
        x_num = 0
        y_num = 0
        for i in range(len(scoring[0])):
            if scoring[0][i] == x_val:
                x_num = i
        for i in range(len(scoring)):
            if scoring[i][0] == y_val:
                y_num = i


        left = dynamic_table[row][col - 1] + int(scoring[len(scoring) - 1][y_num])
        diag = dynamic_table[row - 1][col - 1] + int(scoring[x_num][y_num])
        top = dynamic_table[row - 1][col] + int(scoring[x_num][len(scoring) - 1])

        if (left == diag) and (diag == top):
            x_str = x[-1] + x_str
            y_str = y[-1] + y_str
            x = x[:-1]
            y = y[:-1]

            col -= 1
            row -= 1


        elif (left == top) and (left > diag):
            x_str = "-" + x_str
            y_str = y[-1] + y_str
            y = y[:-1]

            row -= 1

        else:
            if (left > diag) and (left > top):
                x_str = x[-1] + x_str
                y_str = "-" + y_str
                x = x[:-1]

                col -= 1
            elif (diag > left) and (diag > top):
                x_str = x[-1] + x_str
                y_str = y[-1] + y_str
                x = x[:-1]
                y = y[:-1]

                col -= 1
                row -= 1
            elif (top > left) and (top > diag):
                x_str = "-" + x_str
                y_str = y[-1] + y_str
                y = y[:-1]
                
                row -= 1
    if len(x) > 0 and len(y) == 0:
        x_str = x_str[1:]
        y_str = y_str[1:]
        while len(x) > 0:
            x_str = x[-1] + x_str
            y_str = "-" + y_str
            x = x[:-1]
        x_str = x_str[1:]
        y_str = x_str[1:]

    if len(y) > 0 and len(x) == 0:
        x_str = x_str[1:]
        y_str = y_str[1:]
        while len(y) > 0:
            y_str = y[-1] + y_str
            x_str = "-" + x_str
            y = y[:-1]
    x_str = x_str[1:]
    y_str = y_str[1:]



    new_x_str = ""
    for i in x_str:
        new_x_str += i + " "
    new_x_str = new_x_str[:-1]

    new_y_str = ""
    for i in y_str:
        new_y_str += i + " "
    new_y_str = new_y_str[:-1]

    print("x: {0}".format(new_x_str))
    print("y: {0}".format(new_y_str))
    print("Score: {0}".format(dynamic_table[(len(dynamic_table) - 1)][(len(dynamic_table[0]) - 1)]))
    return



def make_new_row(x):
    rows = []
    for i in range(0, len(x)):
        rows.append(0)
    return rows


def dynamic(scoring, x, y, dyn_table, row, col):
    while row != (len(y)):
        x_val = x[col]
        y_val = y[row]
        x_num = 0
        y_num = 0
        for i in range(len(scoring[0])):
            if scoring[0][i] == x_val:
                x_num = i
        for i in range(len(scoring)):
            if scoring[i][0] == y_val:
                y_num = i

        if col == 0 and row == 0:
            dyn_table[row][col] = 0
        elif col < 1 and row != 0:
            idx_score = int(scoring[x_num][y_num]) + int(dyn_table[row - 1][col])
            dyn_table[row][col] = idx_score
        elif row < 1 and col != 0:

            idx_score = int(scoring[x_num][y_num]) + int(dyn_table[row][col - 1])
            dyn_table[row][col] = idx_score

        else:
            top = dyn_table[row - 1][col]
            diag = dyn_table[row - 1][col - 1]
            left = dyn_table[row][col - 1]
            add_value = max((top + int(scoring[x_num][len(scoring) - 1])), (diag + int(scoring[x_num][y_num])), (left + int(scoring[len(scoring) - 1][y_num])))
            dyn_table[row][col] = add_value

        col += 1
        if col == (len(x)):
            col = 0
            row += 1


    return dyn_table






if __name__ == "__main__":
    main()