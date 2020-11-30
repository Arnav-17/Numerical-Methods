import numpy as np

# This function calculates the surface area of function by rotation around x axis

n = int(input('Enter number of divisions\n'))
a = float(input('Initial Value\n'))
b = float(input('Final value\n'))
h = (b - a)/n

"""Tip:- Take the very large n"""


def f(l):
    return l**2

l = 0
for i in range(n):
    l += 2*np.pi*f(a+i*h)*np.sqrt(1 + ((f(a + i*h + h) - f(a + i*h))/h)**2)*h
print(l)


