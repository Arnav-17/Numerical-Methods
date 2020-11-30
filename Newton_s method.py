n = int(input("Enter the number\n"))


def f(x):
    return x**2 - 9


def diff(a, h):
    d = (f(a+h)-f(a-h)) / (2*h)
    return d


# Do not take x_0 = 0


def g(x_0):
    for i in range(n):
        if x_0 == 0:
            continue
        x_0 -= f(x_0)/diff(x_0, 0.001)

    return x_0


print(g(1))





