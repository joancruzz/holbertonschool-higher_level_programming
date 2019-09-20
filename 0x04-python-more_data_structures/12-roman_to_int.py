#!/usr/bin/python
def roman_to_int(roman_string):
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    num = 0
    numeral = rom_str
    if type(rom_str) is not str:
        return None
    if rom_str is None:
        return None
    for num if range (num, len(numeral)):
        if num < len(numeral) - 1 and my_dict[numeral[num]] < my_dict[numeral[num + 1]]:
            value -= my_dict[numeral[num]]
        else:
            value += my_dict[numeral[num]]
    return value
