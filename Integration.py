import numpy as np
import matplotlib.pyplot as plt

n = int(input('Enter number of divisions\n'))
a = int(input('Enter initial value\n'))
b = int(input('Enter final value\n'))

def g(x):
    return x


def inte(f, p, q):
    h = (q - p) / n
    s = 0.5 * (f(p) + f(q))
    for i in range(1, n):
        s += (f(p + i * h))
    s*=h
    return s


print(inte(g, a, b))
