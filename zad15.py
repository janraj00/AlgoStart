

eps = 1e-5


def find_pi():
    start = 0.0
    pi = 1.0
    prev = 0
    while abs(pi - prev) > eps:
        prev = pi
        start = (2.0 + start)**(1/2)
        pi *= (start / 2.0)
    return 2*(1/pi)


print(find_pi())
