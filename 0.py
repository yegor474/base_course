import numpy as np
import math
import constants as cst

t = float(input('n: '))
t = float(input('t: '))
x0 = float(input('x0: '))
y0 = float(input('y0: '))
v0x = float(input('v0x: '))
v0y = float(input('v0y: '))

x = x0 + (v0x*t)
y = y0 + v0y*t-((9.8*t**2)/2)

print(x, y)
for i in range(n):
    print(t[1], x[1], y[1], sep="\t")