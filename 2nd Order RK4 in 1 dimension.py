import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
n = int(input("Enter the number"))
start = timer()


def f(x, u, t):
    return 5


# n = used to incorporate t_n
# h = time interval between t_0 and t_n
# t_0 = initial value of time
# x_0 = initial value of function
# t_n = Time at which we want x_n
# x_n = The value you want at t_n
# t_orig & x_orig are arrays for original graph
# u_0 = initial velocity
# x = distance in x-direction
# u = velocity
# t = time


def func(x_0, u_0, t_0, h):
    x_graph = list()
    t_graph = list()
    u_graph = list()
    for i in range(1, n+1):
        m1 = h*u_0
        k1 = h*f(x_0, u_0, t_0)
        m2 = h*(u_0 + 0.5*k1)
        k2 = h*f(x_0+0.5*m1, u_0+0.5*k1, t_0+0.5*h)
        m3 = h*(u_0 + 0.5*k2)
        k3 = h*f(x_0+0.5*m2, u_0+0.5*k2, t_0+0.5*h)
        m4 = h*(u_0 + k3)
        k4 = h*f(x_0+m3, u_0+k3, t_0+h)
        x_0 += (m1 + 2*m2 + 2*m3 + m4)/6
        u_0 += (k1 + 2*k2 + 2*k3 + k4)/6
        t_0 += h
        x_graph.append(x_0)
        t_graph.append(t_0)
        u_graph.append(u_0)
    plt.plot(t_graph, x_graph)
    plt.show()
    return x_0


print(func(0, 0, 0, 0.001))
end = timer()
print(f"Time taken to complete program is {end - start} seconds")
