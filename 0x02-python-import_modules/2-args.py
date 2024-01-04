#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    out = sys.argv
    outLen = range(1, len(sys.argv))

    for i in outLen:
        print("{}: {}".format(i, out[i]))
