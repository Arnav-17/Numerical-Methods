import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import matplotlib.animation as animation
n = int(input("Enter the number"))
start = timer()


def f(y, t):
    return 10 - 10*t


def g(x, t):
    return 5

# n = used to incorporate t_n
# h = time interval between t_0 and t_n
# t_0 = initial value of time
# x_0 = initial value of function
# t_n = Time at which we want x_n
# x_n = The value you want at t_n
# t_orig & x_orig are arrays for original graph
# g(x,t) is in x direction
# f(y,t) is in y direction


t_orig = np.linspace(0, 10, 10000)
x_orig = 2-5*t_orig**2


def func(x_0, y_0, t_0, h):
    x_n = x_0
    y_n = y_0
    x_graph = []
    y_graph = []
    t_graph = []
    for i in range(1, n + 1):
        k1 = h * f(y_n, t_0)
        l1 = h * g(x_n, t_0)
        k2 = h * f(y_n + 0.5 * k1, t_0 + 0.5 * h)
        l2 = h * g(x_n + 0.5 * l1, t_0 + 0.5 * h)
        k3 = h * f(y_n + 0.5 * k2, t_0 + 0.5 * h)
        l3 = h * g(x_n + 0.5 * l2, t_0 + 0.5 * h)
        k4 = h * f(y_n + k3, t_0 + h)
        l4 = h * g(x_n + l3, t_0 + h)
        y_n += (k1 + 2 * k2 + 2 * k3 + k4)/6
        x_n += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        t_0 += h
        x_graph.append(x_n)
        y_graph.append(y_n)
        t_graph.append(t_0)
    plt.plot(x_graph, y_graph)
    plt.show()
    return x_n, y_n


print(func(0, 0, 0, 0.001))
end = timer()
print(f"Time taken to complete program is {end - start} seconds")
