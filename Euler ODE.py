import numpy as np
import matplotlib.pyplot as plt
n = int(input("Enter the number"))

# Enter your function here


def func(x, t):
    return -np.sqrt(20*(2-x))
# n = used to incorporate t_n
# h = time interval between t_0 and t_n
# t_0 = initial value of time
# x_0 = initial value of function
# t_n = Time at which we want x_n
# x_n = The value you want at t_n
# t_orig & x_orig are arrays for original graph


# t_orig = np.linspace(0, 10, 10000)
# x_orig = 2-5*t_orig**2


def f(h, x_0, t_0):
    x_graph = []
    t_graph = []
    x_n = x_0
    t_n = t_0
    for i in range(n+1):
        t_n = t_0 + i*h
        x_n += h*func(x_n, t_n)
        x_graph.append(x_n)
        t_graph.append(t_n)
    plt.plot(t_graph, x_graph)
    # plt.plot(t_orig, x_orig)
    plt.xlabel('t')
    plt.ylabel('x')
    plt.show()
    return x_n


print(f(0.001, 1.9999, 0))
