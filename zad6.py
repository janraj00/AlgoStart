
eps = 1e-10


def bisect(num=2020):
    left, right = 0, 100  # odpowiednio duża liczba
    while abs(left - right) > eps:
        x = (left + right) / 2
        if x ** x > num:
            right = x
        else:
            left = x
    return left


print(bisect())
