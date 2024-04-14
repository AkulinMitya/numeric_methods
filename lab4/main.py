import math
from sympy import diff, symbols, cos, sin

b = 2
a = 1
length = b - a


def f(x):
    return math.sqrt(x) * math.cos(x * x)


def diff_f(x):
    return (math.cos(x * x) / (2 * math.sqrt(x))) - 2 * math.sin(x * x) * x ** (3 / 2)


def medium_rectangles(h: float):
    m = int(length / h)
    x = a
    res = 0
    for i in range(0, m):
        res += h * f(x + (h / 2))
        x += h
    print(res)


def euler(h: float):
    m = int(length / h)
    x = a
    res = 0

    res += 0.5 * f(a)
    x += h
    for i in range(1, m):
        res += f(x)
        x += h
    res += 0.5 * f(b)
    res *= h
    res += (1 / 12) * h * h * (diff_f(a) - diff_f(b))
    print(res)


def main():
    print("Эйлера")
    euler(0.1)
    euler(0.05)
    euler(0.025)
    print("Средние прямоугольники")
    medium_rectangles(0.1)
    medium_rectangles(0.05)
    medium_rectangles(0.025)


if __name__ == '__main__':
    main()
