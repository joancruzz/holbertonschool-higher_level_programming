#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for num in range(x):
            print(my_list[num], end="")
            num = num + 1
    except IndexError:
        None

    print()
    return num
