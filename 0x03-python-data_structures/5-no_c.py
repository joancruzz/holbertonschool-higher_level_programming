#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for x in range(len(my_string)):
        if (my_string[x] != 'c') and (my_string[x] != 'C'):
            str += my_string[x]
    return(str)
