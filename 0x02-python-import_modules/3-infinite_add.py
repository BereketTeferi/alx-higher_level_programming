#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print(0)
    else:
        for i in range(1, num_args + 1):
            sum += int(sys.argv[i])
        print(sum)
