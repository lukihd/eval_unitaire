def join(string_list, seperator):
    res = ""
    for string in string_list:
        if res != "":
            res = f"{res}{seperator}{string}"
        else:
            res = f"{string}"
    return res

def avg(int_list):
    return sum(int_list)/len(int_list)

