#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    out = sys.argv
    outLen = len(sys.argv)

    if outLen < 4:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit (1)


    """if out[2] != '+' and out[2] != '-' and out[2] != '*' and out[2] != '/':
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)"""
    
    a = int(out[1])
    b = int(out[3])

    add = calculator_1.add(a, b)
    sub = calculator_1.sub(a, b)
    mul = calculator_1.mul(a, b)
    div = calculator_1.div(a, b)

    if out[2] == '+':
        print("{} + {} = {}".format((a), (b), add))
    elif out[2] == '-':
        print("{} - {} = {}".format((a), (b), sub))
    elif out[2] == '*':
        print("{} * {} = {}".format((a), (b), mul))
    elif out[2] == '/':
        print("{} / {} = {}".format((a), (b), div))
    else:
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)
