import numpy as np


def f(x):
    return x**3


def double_diff(a, h):
    p = (f(a + 2 * h) - 2 * f(a) + f(a - 2 * h))/(4 * h ** 2)
    return p


print(double_diff(2, 0.001))
