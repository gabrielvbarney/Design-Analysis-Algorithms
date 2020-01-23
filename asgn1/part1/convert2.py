def convert2():
    merge_open = open("mergeStats2.txt", "r")
    select_open = open("selectStats2.txt", "r")
    merge_open = merge_open.read().strip().split()
    select_open = select_open.read().strip().split()
    print(merge_open)
    print(select_open)
    merge_write = open("mergeStats3.txt", "w")
    select_write = open("selectStats3.txt", "w")
    for i in merge_open:
        merge_write.write(i)
        merge_write.write("\n")
    for i in select_open:
        select_write.write(i)
        select_write.write("\n")

convert2() 
