

def convert():
    merge_open = open("mergeStats.txt", "r")
    select_open = open("selectStats.txt", "r")
    merge_open = merge_open.read()
    select_open = select_open.read()
    temp = " "
    count = 0
    write_merge = open("mergeStats2.txt", "w")
    write_select = open("selectStats2.txt", "w")
    for i in merge_open:
        temp += i
        if i == ".":
            count = 0
        count += 1
        if count == 18:
            temp += " "
            write_merge.write(temp)
            temp = " "
    temp = " "
    for i in select_open:
        temp += i
        if i == ".":
            count = 0
        count += 1
        if count == 16:
            temp += " "
            write_select.write(temp)
            temp = " "
    write_merge.close()
    write_select.close()

convert()


