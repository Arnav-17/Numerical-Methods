def f(x):
    return x**2


def diff(a, h):
    d = (f(a+h)-f(a-h)) / (2*h)
    return d


print(diff(2, 0.001))
