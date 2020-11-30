import numpy as np
n = int(input('Enter number of divisions\n'))
a = float(input('Enter initial value\n'))
b = float(input('Enter final value\n'))
h = (b-a)/n

def f(l):
    return l**2

d = 0 
for i in range(n):
	d += np.sqrt(1 + ((f(a + i*h + h) - f(a + i*h))/h)**2)*h
print(f'Length of the curve = {abs(d)}')