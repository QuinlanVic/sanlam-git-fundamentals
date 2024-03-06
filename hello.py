print("hello")


def double(n):
    return n * 2


print(double(10))


def squared(x):
    return x * x


print(squared(20))


def summing(a, b):
    return a + b


print(summing(double(10), squared(double(10))))
