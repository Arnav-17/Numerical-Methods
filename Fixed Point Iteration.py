n = int(input("Enter the number\n"))


def func(x):
    return 1 + 1/(2*x)


def g(x_0):
    for i in range(n):
        x_0 = func(x_0)
    return x_0


print(g(2))