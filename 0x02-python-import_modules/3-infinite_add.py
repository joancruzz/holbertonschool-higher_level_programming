#!/usr/bin/python3
import sys
args = len(sys.argv)
if __name__ == "__main__":
    sum = 0
    for i in range(1, args):
        sum = sum + int(sys.argv[i])
    print(sum)
