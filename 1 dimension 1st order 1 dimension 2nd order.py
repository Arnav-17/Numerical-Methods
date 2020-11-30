import matplotlib.pyplot as plt
from timeit import default_timer as timer
n = int(input("Enter the number"))
start = timer()


def f(x, u, t):
    return 5


def g(y, t):
    return 5


def func(x_0, u_0, t_0, y_0, h):
    x_graph = list()
    t_graph = list()
    u_graph = list()
    y_graph = list()
    y_n = y_0
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
        l1 = h * g(y_n, t_0)
        l2 = h * g(y_n + 0.5 * l1, t_0 + 0.5 * h)
        l3 = h * g(y_n + 0.5 * l2, t_0 + 0.5 * h)
        l4 = h * g(y_n + l3, t_0 + h)
        y_n += (l1 + 2 * l2 + 2 * l3 + l4) / 6
        t_0 += h
        x_graph.append(x_0)
        t_graph.append(t_0)
        u_graph.append(u_0)
        y_graph.append(y_n)
    plt.plot(y_graph, x_graph)
    # plt.show()
    return x_0, y_n


print(func(0, 0, 0, 0, 0.001))
