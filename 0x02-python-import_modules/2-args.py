#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    out = sys.argv
    outLen = range(1, len(sys.argv))

    if (len(sys.argv) - 1) == 1:
        print("{} argument:".format(len(sys.argv) - 1))
    elif (len(sys.argv) - 1) > 1:
        print("{} arguments:".format(len(sys.argv) - 1))
    else:
        print("{} argument.".format(len(sys.argv) - 1))

    for i in outLen:
        print("{}: {}".format(i, out[i]))
