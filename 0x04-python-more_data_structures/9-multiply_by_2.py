def multiply_by_2(a_dictionary):
    temp = dict(a_dictionary)
    for key in temp:
        temp[key] *= 2
    return temp
