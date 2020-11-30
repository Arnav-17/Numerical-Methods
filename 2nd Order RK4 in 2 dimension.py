import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
n = int(input("Enter the number"))
start = timer()


def f(x, u, t):
    return 5*np.cos(5*t)


def g(y, u_y, t):
    return 5*np.sin(5*t)
# n = used to incorporate t_n
# h = time interval between t_0 and t_n
# t_0 = initial value of time
# x_0 = initial distance in x-direction
# y_0 = initial distance in y-direction
# t_n = Time at which we want x_n
# x_n = The value you want at t_n
# t_orig & x_orig are arrays for original graph
# u_0_x = initial velocity in x-direction
# u_0_y = initial velocity in y-direction
# x = distance in x-direction
# y = distance in y-direction
# u = velocity
# t = time


def func(x_0, u_0_x, y_0, u_0_y, t_0, h):
    x_graph = list()
    t_graph = list()
    u_graph = list()
    u_y_graph = list()
    y_graph = list()
    for i in range(1, n+1):
        m1 = h*u_0_x
        k1 = h*f(x_0, u_0_x, t_0)
        m2 = h*(u_0_x + 0.5*k1)
        k2 = h*f(x_0+0.5*m1, u_0_x+0.5*k1, t_0+0.5*h)
        m3 = h*(u_0_x + 0.5*k2)
        k3 = h*f(x_0+0.5*m2, u_0_x+0.5*k2, t_0+0.5*h)
        m4 = h*(u_0_x + k3)
        k4 = h*f(x_0+m3, u_0_x+k3, t_0+h)
        x_0 += (m1 + 2*m2 + 2*m3 + m4)/6
        u_0_x += (k1 + 2*k2 + 2*k3 + k4)/6
        a1 = h * u_0_y
        b1 = h * g(y_0, u_0_y, t_0)
        a2 = h * (u_0_y + 0.5 * b1)
        b2 = h * g(y_0 + 0.5 * a1, u_0_y + 0.5 * b1, t_0 + 0.5 * h)
        a3 = h * (u_0_y + 0.5 * b2)
        b3 = h * g(y_0 + 0.5 * a2, u_0_y + 0.5 * b2, t_0 + 0.5 * h)
        a4 = h * (u_0_y + b3)
        b4 = h * g(y_0 + a3, u_0_y + a3, t_0 + h)
        y_0 += (a1 + 2 * a2 + 2 * a3 + a4) / 6
        u_0_y += (b1 + 2 * b2 + 2 * b3 + b4) / 6
        t_0 += h
        x_graph.append(x_0)
        t_graph.append(t_0)
        u_graph.append(u_0_x)
        u_y_graph.append(u_0_y)
        y_graph.append(y_0)
        plt.xlabel('x')
        plt.ylabel('y')
    plt.plot(x_graph, y_graph)
    plt.show()
    return x_0, y_0


print(func(0, 0, 0, 0, 0, 0.001))
end = timer()
print(f"Time taken to complete program is {end - start} seconds")
