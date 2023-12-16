def yakobi():
    x_1_k = x_1_0
    x_2_k = x_2_0
    x_3_k = x_3_0
    n = 0
    while True:
        x_1_k1 = (-1.7 + 0.3 * x_2_k - 0.2 * x_3_k) / (-0.6)
        x_2_k1 = (1.41 - 0.1 * x_1_k + 0.2 * x_3_k) / 1.51
        x_3_k1 = 1.6 + 0.1 * x_1_k + 0.1 * x_2_k
        n += 1
        if abs(x_1_k1 - x_1_k) < eps and abs(x_2_k1 - x_2_k) < eps and abs(x_3_k1 - x_3_k) < eps:
            print(x_1_k1, x_2_k1, x_3_k1)
            print("n равно " + str(n))
            break
        x_1_k = x_1_k1
        x_2_k = x_2_k1
        x_3_k = x_3_k1


def g_z():
    x_1_k = x_1_0
    x_2_k = x_2_0
    x_3_k = x_3_0
    n = 0
    while True:
        x_1_k1 = (-1.7 + 0.3 * x_2_k - 0.2 * x_3_k) / (-0.6)
        x_2_k1 = (1.41 - 0.1 * x_1_k1 + 0.2 * x_3_k) / 1.51
        x_3_k1 = 1.6 + 0.1 * x_1_k1 + 0.1 * x_2_k1
        n += 1
        if abs(x_1_k1 - x_1_k) < eps and abs(x_2_k1 - x_2_k) < eps and abs(x_3_k1 - x_3_k) < eps:
            print(x_1_k1, x_2_k1, x_3_k1)
            print("n равно " + str(n))
            break
        x_1_k = x_1_k1
        x_2_k = x_2_k1
        x_3_k = x_3_k1


eps = 0.5 * 10 ** (-4)
x_1_0 = 17 / 6
x_2_0 = 141 / 151
x_3_0 = 16 / 10
yakobi()
g_z()
