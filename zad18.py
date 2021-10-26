eps = 1e-10


def cubic_root(num):
    start = 1
    next_ = start - (start ** 3 - num) / (3 * start ** 2)
    while abs(start - next_) > eps:
        start, next_ = next_, next_ - (next_ ** 3 - num) / (3 * next_ ** 2)
    return next_


print(cubic_root(27))
