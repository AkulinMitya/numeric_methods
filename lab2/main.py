import math

eps = 0.5 * (10 ** -5)


def f(x: float):
    return math.exp(x) - 1.8 + x * x


# Первая производная
def f1(x: float):
    return math.exp(x) + 2 * x


# Вторая производная
def f2(x: float):
    return math.exp(x) + 2


def half_division(a, b):
    x = None
    n = 0
    while abs(b - a) >= eps:
        print(f"step {n}: [{a};{b}]")
        x = (a + b) / 2
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        n += 1
    print(x)


def newton(x0):
    x_n = x0
    n = 1
    while True:
        x_n1 = x_n - (f(x_n) / f1(x_n))
        print(f"x_{n} = {x_n1}")
        if abs(f(x_n)) < eps:
            break
        x_n = x_n1
        n += 1


def modify_newton(x0):
    x_n = x0
    n = 1
    while True:
        x_n1 = x_n - (f(x_n) / f1(x0))
        print(f"x_{n} = {x_n1}")
        if abs(f(x_n)) < eps:
            break
        x_n = x_n1
        n += 1


def not_movement_chord(a, b):
    x0 = b
    x1 = a
    n = 2
    while True:
        x2 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0)))
        print(f"x_{n} = {x2}")
        if abs(f(x2)) < eps:
            break
        x1 = x2
        n += 1


def movement_chord(a, b):
    x0 = b
    x1 = a
    n = 2
    while abs(f(x1)) >= eps:
        x1, x0 = x1 - (f(x1) * (x1 - x0) / (f(x1) - f(x0))), x1
        print(f"x_{n} = {x1}")
        n += 1


def g(x):
    return math.log(1.8 - x ** 2)


def simple_iteration():
    x0 = 0.25
    x1 = g(x0)
    n = 1
    while n <= 25:
        print(f"x_{n} = {x1}")
        x0 = x1
        x1 = g(x0)
        n += 1


def main():
    print(math.log(1.276 * 0.5 * 10**(-5), (50/81)))

    # half_division(0, 1)
    # newton(1)
    # modify_newton(1)
    # not_movement_chord(0, 1)
    # movement_chord(0, 1)
    simple_iteration()

if __name__ == '__main__':
    main()
