#!/usr/bin/python3
def uppercase(str):
    for uppr_lttr in str:
        if ord(uppr_lttr) >= 97 and ord(uppr_lttr) <= 122:
	        dif = 32
        else:
	        dif = 0
        print("{:c}".format(ord(uppr_lttr) - dif), end="")
    print( )
