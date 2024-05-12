import math
import matplotlib.pyplot as plt
import numpy as np

a = 0
b = 1
length = b - a
y_0 = 1


def f_x(y):
    return -4 * (y + 1)


def f_y(x):
    return -4 * x


def f(x, y):
    return -4 * x * (y + 1)


def exact_func(x):
    return 2 * (math.e ** (-2 * x * x)) - 1


def exact_solution(n):
    x = []
    y = []
    h = length / n
    x_i = a
    for i in range(0, n + 1):
        y_i = exact_func(x_i)
        x.append(x_i)
        y.append(y_i)
        x_i += h

    return x, y


def explicit_euler(n):
    x = [a]
    y = [y_0]
    h = length / n
    x_i = a
    y_i = y_0
    for i in range(0, n):
        y_i = y_i + f(x_i, y_i) * h
        x_i += h
        x.append(x_i)
        y.append(y_i)

    return x, y


def koshi(n):
    x = [a]
    y = [y_0]
    h = length / n
    x_i = a
    y_i = y_0
    for i in range(0, n):
        y_half = y_i + h / 2 * f(x_i, y_i)
        y_i = y_i + h * f(x_i + (h / 2), y_half)
        x_i += h
        x.append(x_i)
        y.append(y_i)
    return x, y


def adams3(n):
    x = [a]
    y = [y_0]
    h = length / n
    x_i = a
    y_i = y_0
    y_i = y_i + h * f(x_i, y_i) + h * h / 2 * (f_x(y_i) + f_y(x_i) * f(x_i, y_i)) + (h ** 3) / 6 * (
            -8 * f(x_i, y_i) + f_y(x_i) * f_y(x_i))
    x_i += h
    x.append(x_i)
    y.append(y_i)
    for i in range(2, n + 1):
        y_i = (y_i - 5 / 3 * h * (x_i + h) + h / 12 * (8 * f(x_i, y_i) - f(x_i - h, y[i - 2]))) / \
              (1 + 5 / 3 * h * (x_i + h))
        x_i += h

        x.append(x_i)
        y.append(y_i)
    return x, y


def draw_method(method, name):
    n1 = 3
    n2 = 6
    n3 = 10
    x1, y1 = method(n1)
    x2, y2 = method(n2)
    x3, y3 = method(n3)
    plt.plot(x1, y1, marker='o', label=f'N = {n1}')
    plt.plot(x2, y2, marker='d', label=f'N = {n2}')
    plt.plot(x3, y3, marker='^', label=f'N = {n3}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(name)
    plt.legend()
    plt.grid()
    plt.show()
    # Код ниже для проверки того, что значения y_i меняются в зависимости от N.
    # calculate_mae(y1, y2)
    # calculate_mae(y1, y3)
    # calculate_mae(y2, y3)


def calculate_mae(y_actual, y_calculated):
    mae_list = []
    for actual, calculated in zip(y_actual, y_calculated):
        mae = abs(actual - calculated)
        mae_list.append(mae)
    print(mae_list)


def draw_all_methods(n):
    x1, y1 = explicit_euler(n)
    x2, y2 = koshi(n)
    x3, y3 = adams3(n)
    x4, y4 = exact_solution(n)
    plt.plot(x1, y1, marker='o', label="Явный метод Эйлера")
    plt.plot(x2, y2, marker='d', label='Метод Коши')
    plt.plot(x3, y3, marker='^', label='Метода Адамса-Мултона')
    plt.plot(x4, y4, marker='.', label='Точное решение')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f"Все методы для N = {n}")
    plt.legend()
    plt.grid()
    plt.savefig(f'diff_{n}.png')
    plt.show()


def main():
    # draw_method(exact_solution, "Точное решение")
    # draw_method(explicit_euler, "Явный метод Эйлера")
    # draw_method(koshi, "Метод Коши")
    # draw_method(adams3, "Метод Адамса-Мултона")
    draw_all_methods(10)
    draw_all_methods(20)
    draw_all_methods(30)


if __name__ == '__main__':
    main()
