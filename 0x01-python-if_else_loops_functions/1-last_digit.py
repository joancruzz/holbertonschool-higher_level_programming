#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    number = -number
ld = number % 10
if num < 0:
    ld = -ld
if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, ld))
elif ld == 0:
    print("Last digit of {} is 0 and is 0".format(num, ld))
else:
    print("Last digit of %d is %d and is less than 6 and not 0" % (num, ld))
