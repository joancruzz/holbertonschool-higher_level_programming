#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_copy = number

if number < 0:
    number = -number

last_digit = number % 10

if num_copy < 0:
    last_digit= -last_digit

if last_digit > 5:
        print("Last digit of {:d} is {:d} and is greater than 5".format(num_copy,last_digit))
elif last_digit == 0:
    print("Last digit of {:d} is 0 and is 0".format(num_copy, last_digit))
elif last_digit < 6:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(num_copy, last_digit))
