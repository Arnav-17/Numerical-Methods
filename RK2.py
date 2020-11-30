import numpy as np
import matplotlib.pyplot as plt
n = int(input("Enter the number"))


def g(x, t):
    return 5
# n = used to incorporate t_n
# h = time interval between t_0 and t_n
# t_0 = initial value of time
# x_0 = initial value of function
# t_n = Time at which we want x_n
# x_n = The value you want at t_n


def f(h, x_0, t_0):
    x_graph = []
    t_graph = []
    for i in range(n+1):
        k1 = h*g(x_0, t_0)
        k2 = h*g(x_0 + 0.5*k1, t_0 + 0.5*h)
        x_0 += k2
        t_0 += h
        x_graph.append(x_0)
        t_graph.append(t_0)
    plt.plot(t_graph, x_graph)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.show()
    return x_0


print(f(0.001, 0, 0))
