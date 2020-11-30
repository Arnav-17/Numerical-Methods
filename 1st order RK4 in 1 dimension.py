import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
n = int(input("Enter the number"))
start = timer()
P = 1.225
A = 1
C = 0.47
m = 10


def g(x, t):
    return 10 - 0.5*P*A*C*x**2/m

# n = used to incorporate t_n
# h = time interval between t_0 and t_n
# t_0 = initial value of time
# x_0 = initial value of function
# t_n = Time at which we want x_n
# x_n = The value you want at t_n


def func(x_0, t_0, h):
    x_n = x_0
    x_graph = []
    t_graph = []
    for i in range(1, n + 1):
        l1 = h * g(x_n, t_0)
        l2 = h * g(x_n + 0.5 * l1, t_0 + 0.5 * h)
        l3 = h * g(x_n + 0.5 * l2, t_0 + 0.5 * h)
        l4 = h * g(x_n + l3, t_0 + h)
        x_n += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        t_0 += h
        x_graph.append(x_n)
        t_graph.append(t_0)
    plt.plot(t_graph, x_graph)
    plt.show()
    return x_n


print(func(0, 0, 0.001))
end = timer()
print(f"Time taken to complete program is {end - start} seconds")
