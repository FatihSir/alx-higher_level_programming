#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv) - 1
    sum = 0
    for i in range(1, length + 1):
        sum = sum + int(sys.argv[i])
    print("{}".format(sum))
