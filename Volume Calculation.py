import numpy as np
"""This is the function used to calculate the volume of solid when a function is rotated about y-axis
This Method is called Shell Method.
Assign a = f(x)
For f(x) < 0, take its absolute value
""" 
n = int(input('Enter number of divisions\n'))
a = int(input('Enter initial value\n'))
b = int(input('Enter Final value\n'))


def g(x):
	r = x**2
	t = 2*np.pi*x
	return r*t

h = (b - a) / n

def Volume(f, p, q):
    s = 0.5 * (f(p) + f(q))
    for i in range(n):
        s += h*(f(p + i * h))
    return s/2


print(Volume(g, a, b))