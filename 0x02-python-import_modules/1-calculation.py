#!/usr/bin/python3
import calculator_1
a = 10
b = 5
add = calculator_1.add(a, b)
sub = calculator_1.sub(a, b)
mul = calculator_1.mul(a, b)
div = calculator_1.div(a, b)

print(f"{a} + {b} = {add}")
print(f"{a} - {b} = {sub}")
print(f"{a} * {b} = {mul}")
print(f"{a} / {b} = {div}")

