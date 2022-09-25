import numpy as np

def find_variance(X):

    avg = np.average(X, axis=0)
    var = (1 / len(X)) * (sum((X - avg) ** 2))
    return var

def find_tunel(X, Y, min_var, step, enc_coeff):

    model = np.polyfit(X, Y, 1)
    k = model[0]
    n = n1 = n2 = model[1]

    while sum(k * X + n1 > Y) < enc_coeff * len(Y):
        n1 += step
    while sum(k * X + n2 < Y) < enc_coeff * len(Y):
        n2 -= step

    hills_up = hills_down = 0
    tmp_up = tmp_down = 0

    for i in range(len(Y)):
        if tmp_up == 1 and Y[i] < k * X[i] + n + 0.9 * (n1 - n):
            hills_up += 1
            tmp_up = 0
        if tmp_down == 1 and Y[i] > k * X[i] + n2 + 0.1 * (n - n2):
            hills_down += 1
            tmp_down = 0
        if Y[i] - (k * X[i] + n) >= 0.9 * (n1 - n):
            tmp_up = 1
        if (k * X[i] + n) - Y[i] >= 0.9 * (n - n2):
            tmp_down = 1

    if hills_up >= 2 and hills_down >= 2:
        print("There are enough hills to call it tunnel")
        if find_variance(Y) >= min_var:
            print("Good tunnel")
        else:
            print("Average tunnel")

    k1 = k2 = k

    return k1, n1, k2, n2

def find_support_line(X, Y, interval_percent, boundary_percent, step):

    model = np.polyfit(X, Y, 1)
    k = model[0]
    n = n1 = n2 = model[1]

    while sum(k * X + n1 > Y) < len(Y):
        n1 += step
    while sum(k * X + n2 < Y) < len(Y):
        n2 -= step

    try:

        N = len(X)
        interval_length = interval_percent * N
        interval_num = N / interval_length
        if interval_length - interval_length // 1 > 0 or interval_num - interval_num // 1 > 0:
            raise Exception
        interval_length = int(interval_length)
        interval_num = int(interval_num)
        flag_up = flag_down = 1
        boundary_down = k * X + n2 + boundary_percent * (n1 - n2)
        boundary_up = k * X + n1 - boundary_percent * (n1 - n2)

    except Exception:

        print("Invalid parameters to a function")
        exit()

    for i in range(interval_num):
        indexes = np.array([j for j in range(i * interval_length, (i + 1) * interval_length)])
        A = np.array(Y[indexes])
        if sum(A > boundary_down[indexes]) == interval_length:
            flag_down = 0
        if sum(A < boundary_up[indexes]) == interval_length:
            flag_up = 0

    if flag_up == 1:
        print("There is a top support line")
        return k, n1
    elif flag_down == 1:
        print("There is a bottom support line")
        return k, n2
    else:
        print("No support line or weird function")
        return 0, 0

