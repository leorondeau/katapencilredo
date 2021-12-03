def write(entry, point):
    # point durability: spaces = 0 newlines =0 lower case=-1, uppercase=-2
    # sharpen: replenishes durability
    # erase: removes last occurence of word All characters = -1
    # edit:
    # she sells sea shells
    # print(entry.isupper())
    entry_list = list(entry)
    # print(len(entry_list.isupper()))

    # worn_point = 0
    if point == 0:
        return point

    for i in range(len(entry_list)):

        if entry_list[i].isupper():
            point += -2
            continue
        if entry_list[i].islower():
            point += -1
            continue
        if entry_list[i].isspace():
            point += 0
            continue

    return point

    # return point
    # print("point", point)




# def sharpen()

